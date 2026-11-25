"""Pelican settings shared by every app's manual; the app, its screenshots and its name come from the environment."""

import os

MANUAL_APP = os.environ.get("MANUAL_APP", "cupcake-master")
MANUAL_SCREENSHOTS = os.environ.get("MANUAL_SCREENSHOTS", "")
SITENAME = os.environ.get("MANUAL_TITLE", "Manual")
MANUAL_VERSION = os.environ.get("MANUAL_VERSION", "latest")
SITEURL = ""
RELATIVE_URLS = True
TIMEZONE = "UTC"
DEFAULT_LANG = "en"

PATH = f"content/{MANUAL_APP}"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = []
STATIC_PATHS = []
SLUGIFY_SOURCE = "basename"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
PAGE_ORDER_BY = "order"
DIRECT_TEMPLATES = ["index"]
INDEX_SAVE_AS = "index.html"
TAGS_SAVE_AS = CATEGORIES_SAVE_AS = AUTHORS_SAVE_AS = ARCHIVES_SAVE_AS = ""
CATEGORY_SAVE_AS = TAG_SAVE_AS = AUTHOR_SAVE_AS = ""
FEED_ALL_ATOM = FEED_ALL_RSS = CATEGORY_FEED_ATOM = TRANSLATION_FEED_ATOM = AUTHOR_FEED_ATOM = AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

THEME = "theme/cupcake"
THEME_STATIC_DIR = "theme"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["cupcake_manual"]
MARKDOWN = {
    "extension_configs": {
        "cupcake_manual.shots:ShotExtension": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.attr_list": {},
    },
    "output_format": "html5",
}
