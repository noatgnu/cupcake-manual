# Cupcake manual

The user manual of cupcake-master, built with [Pelican](https://getpelican.com) into an offline site that ships inside
each app and can also be published online.

## Writing pages

Each app's pages are Markdown files in `content/<app>/pages/`, starting with metadata:

```
Title: Backups and restore
Order: 05
Summary: Nightly backups, copying them off the node, and restoring an instance.
Screens: dashboard:backup_storage, dashboard:instance_detail
```

`Screens` lists the app's screens (URL names) the page explains; their **?** opens it. Link to another page with
`[backups]({filename}backups.md)`.

Screenshots come from the apps' client tests, which save captioned screenshots with a `manifest.json`. Show one with
`![](shot:steps-backup/1-instance)`; an empty description uses the screenshot's caption.

## Building

```
poetry install
poetry run python -m manual --app cupcake-master --title "cupcake-master manual" \
  --screenshots <folder with manifest.json> --out dist/cupcake-master --archive dist/cupcake-master.tar.gz
```

The build stops on a missing screenshot or a broken link. It writes the site, `screens.json` (which page explains each
screen) and `search-index.js` (offline search), and converts the screenshots it uses to WebP.

The `.tar.gz` goes into an app at build time; cupcake-master takes it with
`docker build --build-arg MANUAL_BUNDLE_URL=<url of the .tar.gz>` and serves it at `/help/`.

## Screenshots and publishing

The screenshots the manual uses are kept in `screenshots/<app>/`, copied from the client tests' screenshot folder
after a run, so each version of the manual keeps the screenshots of its own release.

- A push to `main` builds the **latest** manual, describing what is in development: its bundle is on the `manual`
  release, which development builds of the apps bake in, and it is online at `<pages>/cupcake-master/latest/`.
- Releasing cupcake-master `vX.Y.Z` (a tag in its repository): tag this repository `cupcake-master-vX.Y.Z` once the
  manual describes that release. The bundle goes on a release of that name, which the image build of `vX.Y.Z` bakes
  in, and the site is kept online at `<pages>/cupcake-master/vX.Y.Z/` next to the earlier versions.

The sites are published on the `gh-pages` branch; GitHub Pages must serve that branch. Online, each manual has a
version menu and says when a newer release exists.

## Tests

```
poetry run pytest
```
