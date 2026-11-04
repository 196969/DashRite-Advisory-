#!/usr/bin/env bash
# Item 381 cleanup — removes the 17 internal files from the public website repo in one commit,
# and replaces sitemap.xml and robots.txt. Run from a fresh clone of 196969/DashRite-Advisory- on main,
# with the extracted package beside it:  bash "3 Beside the package/cleanup.sh" /path/to/clone
set -euo pipefail
PKG="$(cd "$(dirname "$0")/.." && pwd)"
cd "$1"
git pull --ff-only
git rm -- Core-BD-Report-Florida.docx Florida-Dial-Pack.docx bot-config.json decisions.json dial-pack.json florida-intake-queue.json florida100-window3-log.jsonl founders-roster.json item379-report.md make_core_bd_close.js make_dial_pack.js practice-classes.json sweep-after.json sweep-report.json sweep.py w3b.py window3.py
cp "$PKG/1 Website upload/sitemap.xml" sitemap.xml
cp "$PKG/1 Website upload/robots.txt" robots.txt
git add sitemap.xml robots.txt
git commit -m "Remove internal files from the public site; point sitemap and robots at dashriteadvisory.com"
git push
