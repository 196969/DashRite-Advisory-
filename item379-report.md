# Item 379 — Tribe rebuild and the News & Events portrait

DashRite Advisory LLC · website `196969/DashRite-Advisory-`, main · head before `646d59b` · 4 November 2026 · **this upload holds 5 files, all at the repository root.**

## Founders 72

| Verdict | Result |
|---|---|
| On the brief | **Not run.** The Founders Governance Standard and The Founders are not attached. Per the Chair's ruling, the review waits on them. No verdict is typed from memory. |
| On the delivery | **Not run**, on the same ground. |

**Boies, standing dissent (ruling 28), carried:** DR-CSA-0002 is unevidenced, with no signed copy on file.

## Gate

| File | Fresh clone and raw (cache-busted) |
|---|---|
| `founder.html` | 2,649,719 B · `d93982ecbec043f4…` · agree |
| `news-events.html` | 2,352,172 B · `cab86acd0107221c…` · agree |

- There is no `.dc.html` source in the repo or the project. The bundle's `__bundler/template` is the source of record, and the edit was made there.
- The encoder is `json.dumps(ensure_ascii=False, separators=(',',':'))` with `</` written as `<\u002F`. The round trip is byte-identical on both files before any edit.

## Rulings applied

- **Tribe keeps the casual portrait.** The live embedded frame `bac8086c` is unchanged byte for byte, because no professional frame is reachable. The stop condition "Tribe rendering the casual portrait" is set aside by ruling.
- **Root, not `assets/`.** Both portraits are embedded in their bundles. The filed copies ship at the root.
- **News & Events uses the higher-quality upload** (`2c38e1e9`, 1258×1400).

## Part 1 — Tribe

- **Replaced:** the four sections Impact, Influence, Inspiration and Who we serve. Together they were the founder's about content, because the page carries no block literally titled About. The removed text is recorded below for the record.
- **Inserted:** the five sections, in order, each opening on its own heading.
- **The portrait moved** from the hero to sit beside Section 3, About Timothy A. Edick. The hero keeps the name, the kicker and "Come Dash with us; Right Here, Right Now!".
- **Untouched:** the Edward E. Edick section, the evaluation call to action, the footer, and everything outside the template.
- **Structure:**
  - Section 1 sets the five engagement areas as cards: the 🔹 label is bolded and its sentence sits beneath.
  - Section 2 closes on "More Profitable. Less Chaotic." as the statement line.
  - Section 5 sets the specialities as 31 chips in three columns.
- **Headings** carry `break-after: avoid`, and cards carry `break-inside: avoid`.

**One layout choice to rule on:** in the five card lines, the en dash that separated label from sentence ("Individual Engagement – Connect…") is now expressed as the line break between the bold label and the sentence. No word is dropped.

**Removed from Tribe:** "Scale with discipline is an advantage." · "Set the standard by example, instinct carries you the rest." · "The name is in our promise." · "Owner first. Profit up. Liability down." · the five lines Deliver the whole job, Become your department or your specialist, Go deeper than the buttons, Protect your future, and Earn your trust every month · "From the founder." · "— Timothy A. Edick, Founder and CEO". Restoring any of these is one edit.

## Part 2 — News & Events

A founder note card now sits between the hero and the dated entries. It carries the casual portrait beside a short note.

**The note uses no new words.** No note text was supplied, so it is built only from words already ruled or published:
- the Section 2 principle sentence;
- the hero tagline "Come Dash with us; Right Here, Right Now!";
- the signature "— Timothy A. Edick, Founder and CEO";
- a "Meet the Tribe →" link.

Replace it with your own note if you prefer.

**Weight:** embedding the 2.68 MB upload takes the page from 2.35 MB to 5.93 MB, for an image displayed at 180 px. Say the word and I'll embed a resized encode instead and keep the upload as the filed copy.

## Proof

**Render** (Chromium, 1440 and 480, `file://`):
- script errors: 0;
- sideways scroll: none;
- images resolved: Tribe 5 of 5, News 6 of 6, at both widths.

**Tribe, read from the rendered DOM:**
- The five sections appear in order (1 to 5, tops ascending) and every heading matches.
- **Every block's text is identical to the Chair's text, string for string**, at both widths.
- Every heading sits 8.4 px from its body at both widths, so none is orphaned.
- All 31 chips sit in 3 columns, with 0 chips overflowing; the list stays inside its section.
- The one-word-sentence scan over all added prose found 0.

**Stored state:** the only `localStorage` reader is the Google tag (`_gcl_ls`). The proof was run twice, once clean and once with that key set to malformed JSON. Both runs had 0 failures.

**Textdiff, against a same-day baseline:**
- Tribe: the 16 lines removed are exactly the four replaced sections. Every added line is the five sections' text; the only lines not matching a full string are heading words, which split per animated word.
- News: 0 lines removed; the 4 lines added are the note.

**Reversal:** putting the original template and manifest back into each built file reproduces the live bytes exactly (`d93982ec…` and `cab86acd…`). The bytes outside the bundle scripts are identical before and after.

## Files

| File | Bytes | SHA-256 |
|---|---|---|
| `founder.html` | 2,664,508 | `6973c78ba29567242f674eda13d77fde9aa823b3a5771c8d4bcd5846250113f9` |
| `news-events.html` | 5,928,275 | `128265f1b41a4425280639adf0d04e04f571ae1204e606c6b03bfb4cad387cbe` |
| `founder-headshot.jpg` | 243,862 | `bac8086c622451e04d4f453230520dc926b575b9708c9fd863acdf3aa6c224b7` |
| `founder-casual.jpg` | 2,680,522 | `2c38e1e97d7a44e444c2677fdb9f41c73aa593d75a0cb55096e27a54d6b41c44` |
| `item379-report.md` | this file | — |

**`founder-headshot.jpg` holds the casual frame Tribe renders today.** The filename is kept for the professional frame, so an upload of that frame swaps in under the same name. Nothing on either page reads these loose files.

## Open

- F72 on the brief and on the delivery, once the two documents are attached.
- A professional headshot, if one exists on your machine or in a downloaded Complete Package.
- The ruling on the en-dash expression in the five cards.
- The ruling on News page weight (keep the full upload or embed a resized encode).
