"""Building a manual with Pelican: screenshots become captioned WebP figures, broken links and missing screenshots
stop the build, and the screen-to-page map and offline search index are written."""

import json
import shutil
from pathlib import Path

import pytest
from PIL import Image

from manual.__main__ import main

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def project(tmp_path, monkeypatch):
    shots = tmp_path / "shots"
    for name in ("screens/01-instances", "steps-backup/1-instance"):
        (shots / name).parent.mkdir(parents=True, exist_ok=True)
        image = Image.new("RGB", (1600, 900), "white")
        image.paste((30, 40, 50), (0, 0, 1600, 300))
        image.save(shots / f"{name}.png")
    (shots / "manifest.json").write_text(json.dumps({"label": "0.0.40", "screenshots": [
        {"file": "screens/01-instances.png", "caption": "The Instances page.", "name": "01-instances", "lineup": "screens"},
        {"file": "steps-backup/1-instance.png", "caption": "Back up now.", "name": "1-instance", "lineup": "steps-backup"},
    ]}))
    pages = ROOT / "content" / "test-app" / "pages"
    pages.mkdir(parents=True)
    yield shots, pages, tmp_path / "out"
    shutil.rmtree(ROOT / "content" / "test-app")


def write(pages, name, text):
    (pages / f"{name}.md").write_text(text)


def build(shots, out):
    return main(["--app", "test-app", "--title", "Test manual", "--screenshots", str(shots), "--out", str(out),
                 "--archive", str(out.parent / "site.tar.gz")])


def test_a_manual_is_built_with_figures_links_screens_and_search(project):
    shots, pages, out = project
    write(pages, "instances", "Title: Instances\nOrder: 01\nSummary: All of them.\nScreens: dashboard:index, "
          "dashboard:instance_detail\n\n![](shot:screens/01-instances)\n\nSee [backups]({filename}backups.md).\n")
    write(pages, "backups", "Title: Backups\nOrder: 02\nSummary: Keep copies.\nScreens: dashboard:instance_detail\n\n"
          "Back up <script>x</script> often.\n\n![Choose it](shot:steps-backup/1-instance)\n")
    assert build(shots, out) == 0
    page = (out / "instances.html").read_text()
    assert 'src="img/screens--01-instances.webp"' in page and "<figcaption>The Instances page.</figcaption>" in page
    assert 'href="./backups.html"' in page or 'href="backups.html"' in page
    assert Image.open(out / "img" / "screens--01-instances.webp").format == "WEBP"
    trimmed = Image.open(out / "img" / "screens--01-instances.webp")
    assert trimmed.width == 1400 and trimmed.height == round((300 + 24) * 1400 / 1600)
    screens = json.loads((out / "screens.json").read_text())
    assert screens["screens"] == {"dashboard:index": "instances.html", "dashboard:instance_detail": "instances.html"}
    assert screens["screenshots_label"] == "0.0.40"
    index = (out / "search-index.js").read_text()
    assert index.startswith("window.MANUAL_INDEX = ") and "Keep copies." in index
    assert [p.name for p in (out.parent).glob("site.tar.gz")]


def test_a_missing_screenshot_stops_the_build(project):
    shots, pages, out = project
    write(pages, "instances", "Title: Instances\nOrder: 01\n\n![](shot:screens/02-gone)\n")
    assert build(shots, out) != 0


def test_a_broken_link_stops_the_build(project):
    shots, pages, out = project
    write(pages, "instances", "Title: Instances\nOrder: 01\n\n[gone]({filename}nowhere.md)\n")
    assert build(shots, out) != 0
