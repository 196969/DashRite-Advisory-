# Item 381 — website exposure cleanup (step 1 of 4)

DashRite Advisory LLC · website `196969/DashRite-Advisory-`, main · head `0459d9e` · 4 November 2026

**This report travels beside the package.** It is not part of any upload set, and it must not be uploaded to any repository the web serves.

## Status, plainly

Once the cleanup upload is applied, the 17 internal files stop being served from dashriteadvisory.com.

**The exposure is then reduced, not closed:**
- **The files stay readable in the public repo's history**, on GitHub, until the fresh-repo migration (step 2) replaces this repository and the old one is retired.
- **Copies outside the repo:** I cannot see whether any fork, clone, cache or archive holds them, so that is stated as unknown rather than as clean.
- **CDN lag:** removed files may keep serving from GitHub Pages' CDN for a short time after the push.

## Register — two faults

**Fault 1. A build report was shipped inside the upload set and published to the public web.**
- *What happened:* in Item 379 I packaged `item379-report.md` with the files for the repository root. It was uploaded with them, and dashriteadvisory.com served it publicly.
- *The cause:* the upload set was built as "everything for this item" rather than "only what the site serves".
- *The standing rule now:* an upload set contains only what the site serves; reports, scripts and working files travel beside it.
- *How it was caught:* by my own post-upload repo check.

**Fault 2. Internal lead data was served from the company domain, because the website repository held files the website does not serve.**
- *What happened:* GitHub Pages publishes every file in the repo, not only the pages. Call lists naming decision-makers with phone numbers and emails, pipeline reads and logs, governance records, F72 ballots and build scripts were all publicly downloadable from dashriteadvisory.com.
- *Verified by direct fetch:* `dial-pack.json`, `Florida-Dial-Pack.docx` and `item379-report.md` each returned 200 from the domain.
- *The cause:* the website repository was used as a working store.
- *The rule:* the website repository holds pages, the assets those pages use, the sitemap, robots and CNAME, and nothing else.

## Classification — every file in the repo (115)

| Class | Files | Fate |
|---|---|---|
| Bundled site pages | 17 | stay |
| State market sheets (`state-*.html`, linked from `states.html`) | 27 | stay |
| Redirect stubs to HOT Leads (`<market>.html`, `<market>-expansion.html`; no lead data on them) | 48 | stay |
| `DashRite-Business-Health-Assessment.pdf` (linked from 15 pages) | 1 | stays |
| `CNAME`, `sitemap.xml`, `robots.txt` | 3 | stay; sitemap and robots replaced |
| `founder-headshot.jpg`, `founder-casual.jpg` (filed copies, per the Item 379 ruling) | 2 | stay |
| **Internal** | **17** | **removed** |

The 17 internal files:
- **Lead data:** `dial-pack.json`, `Florida-Dial-Pack.docx`, `florida-intake-queue.json`, `florida100-window3-log.jsonl`.
- **Governance and F72:** `decisions.json`, `founders-roster.json`, `sweep-report.json`, `sweep-after.json`, `Core-BD-Report-Florida.docx`, `bot-config.json`, `practice-classes.json`.
- **Build scripts:** `sweep.py`, `w3b.py`, `window3.py`, `make_dial_pack.js`, `make_core_bd_close.js`.
- **Report:** `item379-report.md`.

**Nothing removed is referenced by any page.** I searched every page, including bundled templates and scripts, for each filename before classing it as internal.

## The package

- **`1 Website upload/`** (flat; only what the site serves): `sitemap.xml` (all 17 URLs now on `https://dashriteadvisory.com/`, valid XML) and `robots.txt` (the Sitemap line now on the domain; nothing else changed).
- **`2 Private repo upload/`** (flat): the 17 internal files, byte-identical to HEAD `0459d9e`.
- **`3 Beside the package/`**: this report, and `cleanup.sh`.

## Where the internal files go

**A new private repository, not `dash-api`.**
- `dash-api` is private: an anonymous read is refused, while `hotleads-repo` and `dash-app-` answer one.
- But `dash-api` is built to deploy on Vercel. As I understand Vercel's behaviour, a project with no framework preset serves the files in its root publicly beside the `api/` functions. Placing the data there would make it public-facing the day the backend is deployed. Please check that against Vercel's current docs before relying on my reading.
- Under your ruling, that sends the data to a new private repo. I propose `196969/dashrite-internal`: private, with Pages never enabled.
- Creating the repo is yours; I have no GitHub access.

## How to apply it, in this order

1. **Create the private repo** and upload `2 Private repo upload/` into it, flat. Confirm all 17 files are there before step 2, so nothing is lost.
2. **Remove the files from the website repo.**
   - *With git:* run `bash "3 Beside the package/cleanup.sh" /path/to/fresh-clone`. It deletes the 17 files, copies in the new sitemap and robots, and pushes as one commit. I dry-ran it on a scratch clone: 19 files changed (17 deleted, 2 modified). Left after: 92 pages, plus `CNAME`, the PDF, the two portraits, `robots.txt` and `sitemap.xml`.
   - *Web only:* the upload button cannot delete. As far as I know, the GitHub web interface deletes one file per commit, from each file's ⋯ menu. That is 17 deletions, then upload `1 Website upload/` for sitemap and robots.
3. **Tell me when it's done.** I'll re-clone and fetch each of the 17 from the domain, and the item closes only when every one returns 404.

## Flags for the next steps — not acted on

**For step 2 (fresh repo): the site is not 17 pages.**
- It serves 92: the 17 bundled pages, plus 27 state sheets that `states.html` links to, plus 48 redirect stubs that forward old market links to HOT Leads.
- A clean repo holding only the 17 would break every link from `states.html` to a state sheet, and every old market link.
- **Please rule:** do the 27 state sheets and the 48 stubs move too?
- Also: 44 pages still name `196969.github.io/DashRite-Advisory-` (canonical tags and links). The fresh repo is the right pass to move them to the domain. The pages and sitemap disagree until then; the old address redirects, so nothing breaks.

**The same exposure, outside this repo.** These sit squarely under your test.
- **`hotleads-repo`, the HOT Leads library, is publicly served at `196969.github.io/hotleads-repo/`, with no noindex.**
  - `florida.html` names 132 decision-makers across 150 rows; `florida-expansion.html` names 38 across 43.
  - Other markets checked carry company phones (`arizona.html`: 54 numbers, no named decision-makers).
  - The stubs this cleanup keeps point visitors to it.
- **`dash-app-`, Dash CRM holding the firm's real books, is publicly served at `196969.github.io/dash-app-/`.** The live page contains the Everlast client name and invoice 1004.

**Neither is changed by this package.** Both want their own ruling: private, gated, or accepted as public by decision.
