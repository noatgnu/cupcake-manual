"""Pelican plugin for the Cupcake manuals: screenshots, the screen-to-page map and the offline search index."""

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageChops
from pelican import signals

from .shots import STATE, reset, shot_file

IMAGE_WIDTH = 1400
COLLECTED = {"pages": []}


class ManualProblem(Exception):
    """The manual refers to something that does not exist."""


def _start(pelican):
    reset()
    COLLECTED["pages"] = []


def _collect(generator):
    COLLECTED["pages"] = sorted(generator.pages, key=lambda page: getattr(page, "order", "99"))


def _plain(content):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", content))).strip()


def _trim(image):
    """The screenshot without the empty page below its content, keeping a small margin."""
    rgb = image.convert("RGB")
    background = Image.new("RGB", rgb.size, rgb.getpixel((rgb.width - 1, rgb.height - 1)))
    box = ImageChops.difference(rgb, background).getbbox()
    if not box:
        return rgb
    return rgb.crop((0, 0, rgb.width, min(rgb.height, box[3] + 24)))


def _convert(source, target):
    with Image.open(source) as original:
        image = _trim(original)
        if image.width > IMAGE_WIDTH:
            image = image.resize((IMAGE_WIDTH, round(image.height * IMAGE_WIDTH / image.width)))
        image.convert("RGB").save(target, "WEBP", quality=82, method=6)


def _finish(pelican):
    if STATE["missing"]:
        raise ManualProblem("No screenshot " + ", ".join(sorted(STATE["missing"])))
    output = Path(pelican.output_path)
    (output / "img").mkdir(parents=True, exist_ok=True)
    folder = Path(pelican.settings["MANUAL_SCREENSHOTS"])
    for name in sorted(STATE["used"]):
        _convert(folder / STATE["shots"][name]["file"], output / "img" / shot_file(name))
    screens, index = {}, []
    for page in COLLECTED["pages"]:
        for screen in filter(None, (s.strip() for s in getattr(page, "screens", "").split(","))):
            screens.setdefault(screen, page.url)
        index.append({"url": page.url, "title": page.title, "summary": _plain(getattr(page, "summary", "")),
                      "text": _plain(page.content)})
    (output / "screens.json").write_text(json.dumps({
        "app": pelican.settings["MANUAL_APP"],
        "built": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "screenshots_label": STATE["label"],
        "screens": screens,
    }, indent=1))
    (output / "search-index.js").write_text("window.MANUAL_INDEX = " + json.dumps(index) + ";\n")
    for name in sorted(set(STATE["shots"]) - STATE["used"]):
        print(f"manual: screenshot {name} is not used by any page")


def register():
    signals.initialized.connect(_start)
    signals.page_generator_finalized.connect(_collect)
    signals.finalized.connect(_finish)
