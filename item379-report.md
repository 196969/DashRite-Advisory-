# Item 379 — Tribe rebuild and News & Events portrait (revision 2)

DashRite Advisory LLC · website `196969/DashRite-Advisory-`, main · head before `646d59b` · 4 November 2026 · **this upload holds 5 files, all at the repository root.** It supersedes the first Item 379 package; do not upload that one.

## Founders 72

| Verdict | Result |
|---|---|
| On the brief | **Not run.** The Governance Standard and The Founders are not attached; the review waits on them, as ruled. |
| On the delivery | **Not run**, on the same ground. |

**Boies, standing dissent (ruling 28), carried:** DR-CSA-0002 is unevidenced, with no signed copy on file.

## What changed in revision 2

**Wording:** all five sections now carry the Chair's power wording from the 4 November message, verbatim.
- **The Principle** has two sentences beneath its lead line, then the closing statement line.
- **Specialities** is reduced to the Chair's ten terms, set as two columns. Ten chips in three columns would leave one chip alone on the last row, so two columns gives five full rows.

**Orphan words, everywhere on both pages:**
- The last two words of every paragraph, list item and label are joined with a non-breaking space. That is 38 sites on Tribe and 18 on News, covering the Edward section, the call to action and every News entry.
- `text-wrap: pretty` is set as a second guard.
- The last two words of every new heading are kept together.
- "Rent-A-Center" and "$168 million" never split across a line.
- **No word outside the five sections changed.** The word stream from Edward's section to the footer on Tribe, and from the first entry to the footer on News, is identical before and after.

**Engagement cards:** the five cards are now full-width rows with the label beside its sentence. At five narrow columns, "Business & Leadership Development" ran to three one-word lines and the 🔹 broke onto a line of its own. Every label now sits on one line at every width measured, with none overflowing.

**News & Events:** the founder note now quotes the new principle sentence.

## The reference screenshots

The three orphans visible in the submitted screenshots are gone: "growth." (What We Offer), "Welders." (About), and "goals." (Leader). None renders as a line of its own.

## Proof

**Orphan instrument:**
- It measures every visible text block on the page. A line is an orphan when it holds one word and is the last of two or more lines.
- **Tested first against a case with a known answer:** on the live Tribe page it finds 4 orphans, at 768, 480 and 390 px, so it can fail.
- **On the build:** 0 orphans across both pages at 1440, 1280, 1024, 768, 600, 480 and 390 px. That covers 104 text blocks on Tribe and 71 on News at desktop widths.

**Verbatim:** at 1440 and 480, every block in the five sections is identical to the Chair's text, string for string. The non-breaking spaces are normalised before comparing.

**Layout:**
- The five sections appear in order, and every heading sits 8.4 px from its body.
- There are 10 chips in 2 columns, with 0 overflowing.
- The one-word-sentence scan found 0.

**Render:**
- script errors: 0;
- sideways scroll: none;
- images resolved: Tribe 5 of 5, News 6 of 6, at both widths.

**Stored state:** the only `localStorage` reader is the Google tag. The proof was run twice, once clean and once with `_gcl_ls` set to malformed JSON. Both runs had 0 failures.

**Reversal:** putting the original template and manifest back into each built file reproduces the live bytes exactly. The bytes outside the bundle scripts are identical before and after.

## Rulings carried

- Tribe keeps the casual portrait (`bac8086c`, unchanged) until a professional frame is uploaded.
- Images are embedded in their bundles; the loose copies ship at the root, not in `assets/`.
- News & Events uses the higher-quality upload (`2c38e1e9`).
- `founder-headshot.jpg` holds the casual frame Tribe shows today; the name is reserved for the professional swap.

## Files

| File | Bytes | SHA-256 |
|---|---|---|
| `founder.html` | 2,658,776 | `f6049b567e94d3a195c8ab75769ae833dc4db30402f9272ea7f5f03732904e3d` |
| `news-events.html` | 5,928,344 | `355bfcf333f6d691248017862c3d0c92e136042ce5c9846d354204c5e80a512a` |
| `founder-headshot.jpg` | 243,862 | `bac8086c622451e04d4f453230520dc926b575b9708c9fd863acdf3aa6c224b7` |
| `founder-casual.jpg` | 2,680,522 | `2c38e1e97d7a44e444c2677fdb9f41c73aa593d75a0cb55096e27a54d6b41c44` |
| `item379-report.md` | this file | — |

## Open

- F72 on the brief and on the delivery, once the two documents are attached.
- A professional headshot, if one exists.
- News page weight: 5.93 MB with the full upload embedded. A resized encode is available on your word.
- Edward's section, the call to action and the News entries keep their existing wording, with orphans fixed. Say so if the power-wording pass should extend to them.
