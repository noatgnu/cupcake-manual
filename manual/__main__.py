"""Build one app's manual with Pelican into an offline site, and optionally a .tar.gz of it.

  python -m manual --app cupcake-master --title "cupcake-master manual" --screenshots <folder> --out dist/cupcake-master
"""

import argparse
import os
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--app", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--screenshots", required=True, help="folder with the client tests' manifest.json")
    parser.add_argument("--out", required=True)
    parser.add_argument("--archive", help="also write the site as a .tar.gz with index.html at its top")
    args = parser.parse_args(argv)
    env = {**os.environ, "MANUAL_APP": args.app, "MANUAL_TITLE": args.title,
           "MANUAL_SCREENSHOTS": str(Path(args.screenshots).resolve())}
    out = Path(args.out).resolve()
    result = subprocess.run(
        [sys.executable, "-m", "pelican", "--settings", "pelicanconf.py", "--output", str(out),
         "--delete-output-directory", "--fatal", "warnings"],
        cwd=ROOT, env=env,
    )
    if result.returncode != 0:
        return result.returncode
    if args.archive:
        with tarfile.open(args.archive, "w:gz") as archive:
            for item in sorted(out.iterdir()):
                archive.add(item, arcname=item.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
