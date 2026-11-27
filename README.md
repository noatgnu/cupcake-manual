# Cupcake manual

The user manuals of Cupcake, Cupcake Vanilla and cupcake-master, built with [Pelican](https://getpelican.com) into
offline sites that ship inside each app and are also published online.

## Writing pages

Each app's pages are Markdown files in `content/<app>/pages/`, starting with metadata:

```
Title: Backups and restore
Order: 05
Summary: Nightly backups, copying them off the node, and restoring an instance.
Screens: dashboard:backup_storage, dashboard:instance_detail
```

`Screens` lists the app's screens the page explains, and their **?** opens it: URL names for cupcake-master, route
paths such as `metadata-tables/:id` for Cupcake and Cupcake Vanilla. `Appliance: yes` marks a page about what only a
Cupcake appliance has. Link to another page with
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

The `.tar.gz` goes into an app at build time with `--build-arg MANUAL_BUNDLE_URL=<url of the .tar.gz>`: cupcake-master's
image, and the cupcake-vanilla-ng and cupcake-webgui frontend images, serve it at `/help/`. The Cupcake appliance image
adds both apps' manuals to its frontends.

## Screenshots and publishing

The screenshots the manual uses are kept in `screenshots/<app>/`, copied from the client tests' screenshot folder
after a run, so each version of the manual keeps the screenshots of its own release.

- A push to `main` builds the **latest** manuals, describing what is in development: their bundles are on the
  `manual` release, which development builds of the apps bake in, and they are online at `<pages>/<app>/latest/`.
- Releasing an app: tag this repository once its manual describes that release. The bundle goes on a release of that
  name, which the app's image build of the same version bakes in, and the site is kept online at
  `<pages>/<app>/<version>/` next to the earlier versions.

| App | Follows | Tag |
|---|---|---|
| cupcake-master | its release tags, such as `v0.0.6` | `cupcake-master-v0.0.6` |
| Cupcake | the backend's (`cupcake_vanilla`) release tags, such as `0.0.34` | `cupcake-0.0.34` |
| Cupcake Vanilla | the backend's release tags | `cupcake-vanilla-0.0.34` |

Every version is kept on the `gh-pages` branch, and each run deploys that branch to GitHub Pages, whose source is
GitHub Actions. Online, each manual has a
version menu and says when a newer release exists.

## Tests

```
poetry run pytest
```
