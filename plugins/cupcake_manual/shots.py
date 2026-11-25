"""Markdown extension turning ![description](shot:<folder>/<name>) into a captioned figure of that screenshot."""

import html
import json
import os
import re
from pathlib import Path

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

SHOT = re.compile(r"!\[([^\]]*)\]\(shot:([A-Za-z0-9_./-]+)\)")
STATE = {"shots": None, "label": None, "used": set(), "missing": set()}


def shot_file(name):
    return name.replace("/", "--") + ".webp"


def manifest():
    """The screenshots the client tests wrote, by folder/name, read once per build from MANUAL_SCREENSHOTS."""
    if STATE["shots"] is None:
        folder = Path(os.environ.get("MANUAL_SCREENSHOTS", ""))
        data = json.loads((folder / "manifest.json").read_text()) if (folder / "manifest.json").is_file() else {}
        STATE["shots"] = {shot["file"].removesuffix(".png"): shot for shot in data.get("screenshots", [])}
        STATE["label"] = data.get("label")
    return STATE["shots"]


def reset():
    STATE.update(shots=None, label=None, used=set(), missing=set())


class ShotPreprocessor(Preprocessor):
    def run(self, lines):
        shots = manifest()

        def figure(match):
            alt, name = match.group(1).strip(), match.group(2)
            if name not in shots:
                STATE["missing"].add(name)
                return ""
            STATE["used"].add(name)
            caption = alt or shots[name]["caption"]
            return (f'\n<figure class="shot"><img src="img/{shot_file(name)}" alt="{html.escape(caption, quote=True)}"'
                    f' loading="lazy"><figcaption>{html.escape(caption)}</figcaption></figure>\n')

        return SHOT.sub(figure, "\n".join(lines)).split("\n")


class ShotExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(ShotPreprocessor(md), "cupcake_shots", 30)
