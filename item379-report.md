# Item 379 — Tribe rebuild and News & Events portrait (revision 3)

DashRite Advisory LLC · website `196969/DashRite-Advisory-`, main · head before `646d59b` · 4 November 2026 · **this upload holds 5 files, all at the repository root.** It supersedes revisions 1 and 2.

## Founders 72

| Verdict | Result |
|---|---|
| On the brief | **Not run.** The Governance Standard and The Founders are not attached. |
| On the delivery | **Not run**, on the same ground. |

**Boies, standing dissent (ruling 28), carried:** DR-CSA-0002 is unevidenced, with no signed copy on file.

## The four rulings, applied

**1 · News page weight.** A resized frame is now embedded: 540×601, JPEG quality 86 with no chroma subsampling, 77,230 bytes, `97670e55…`. That is three times the 180 px display width, so it stays sharp on high-density phones. The News page falls from 5.93 MB to 2.46 MB; it was 2.35 MB live before this item. The full-size upload ships unchanged at the root as `founder-casual.jpg`.

**2 · Edward's section and the call to action, in power wording.** The headings, kicker, email line, buttons and "Two seats. One standard. Built RITE!" are unchanged.

**No fact was added or dropped.** Everything carried before is still stated: the second seat, the 25 years in sales, operations and business development, the middle-management conviction, Florida portfolio operations, fractional leadership, acquisitions and private equity forming under his seat, the front of the house reporting to the Chair, and the free evaluation, written findings and fixed number. "Upcoming" now reads "forming", matching the News entry of 25 October.

| Was | Now |
|---|---|
| Edward holds the second seat at DashRite Advisory, and he carries it where the work is won: in the room, across the table, in front of the owner. Twenty-five years of senior leadership in sales, operations and business development stand behind him, and the pattern never changes. He walks into an operation, finds the people who actually move the numbers, and builds the structure that lets them. | Edward holds DashRite’s second seat and works where deals are won: in the room, across the table, face to face with the owner. Twenty-five years of senior leadership in sales, operations and business development back him. He finds the people who move the numbers and builds the structure that frees them. |
| Edward built his reputation on a conviction most firms say and few operate on: organisations succeed or fail on the strength of their middle management. Strategy written at the top is only as good as the layer asked to carry it. He strengthens that layer first, then the plan holds, the quarter lands, and the improvement survives the consultant leaving the building. | Edward’s conviction is simple: organisations rise or fall on their middle management. Strategy is only as strong as the layer that carries it. He strengthens that layer first, so the plan holds, the quarter lands and the gains outlast the engagement. |
| Portfolio operations across Florida, with upcoming fractional leadership, acquisitions, and private equity under his seat. He carries the front of the house — the firms, the conversations, the relationships — and brings what he finds back to the Chair. Every engagement still opens the same way it always has: a free evaluation, real findings in writing, and a fixed number before anything moves. | Edward commands portfolio operations across Florida, with fractional leadership, acquisitions and private equity forming under his seat. He runs the front of the house and brings every finding back to the Chair. Every engagement opens the same way: a free evaluation, real findings in writing and a fixed number before anything moves. |
| Real findings, a scope in writing and a fixed number. You decide from there, and nothing moves until you do. | Real findings. A scope in writing. A fixed number. You decide, and nothing moves until you do. |
| Spend sixty seconds on the Business Health Assessment and find out where your operation is losing money. Nothing is asked of you, no call is booked, and the answer is yours to keep. | Spend sixty seconds on the Business Health Assessment and see where your operation is losing money. No ask, no booked call, and the answer is yours to keep. |

**3 · News entries.** Not reworded. Their word stream from the first entry to the footer is identical before and after; only the orphan glue was added.

**4 · Headshot slot.** Kept as built.

## A tightening found by a stricter instrument

Ruling 2 asked for **no one-word lines**, which is stricter than no orphans. So I extended the instrument to flag a one-word line anywhere in a block, not only the last line.

- **Tested first against a case with a known answer:** on the live Tribe page it finds 7.
- **It found 1 site in the build.** At 480 and 390 px, the chip "Multi-Unit Operations Command" broke after "Multi-Unit".
- **The fix:** the chips now sit in 2 columns on desktop and stack to 1 column below roughly 660 px. "Twenty-five" and "Twenty-plus" are also kept from splitting at their hyphens.

## Proof

**One-word lines:** 0 on both pages at 1440, 1280, 1024, 768, 600, 480 and 390 px. The instrument checks every visible text block on every line.

**Verbatim:** at 1440 and 480, every block in the five sections is identical to the Chair's text, string for string.

**Layout:**
- The five sections appear in order, and every heading sits 8.4 px from its body.
- There are 10 chips, in 2 columns at 1440 and 1 at 480, with 0 overflowing.
- The one-word-sentence scan over all new and reworded prose found 0.

**Render:**
- script errors: 0;
- sideways scroll: none;
- images resolved: Tribe 5 of 5, News 6 of 6, at both widths.

**Stored state:** the proof was run twice, once clean and once with `_gcl_ls` set to malformed JSON. Both runs had 0 failures.

**Unchanged regions:** Tribe's header and footer words are unchanged, and so are the words of every News entry.

**Reversal:** putting the original template and manifest back into each built file reproduces the live bytes exactly.

## Files

| File | Bytes | SHA-256 |
|---|---|---|
| `founder.html` | 2,658,635 | `dc5275f9c37b5aba664a0e35306cd6a3ad93e527774d81c83317e891e506b17b` |
| `news-events.html` | 2,457,288 | `1e962f67b5ea77dba1dc8a8d8d02a85be040e3de3f63387ab2d5f9efc4d8d807` |
| `founder-headshot.jpg` | 243,862 | `bac8086c622451e04d4f453230520dc926b575b9708c9fd863acdf3aa6c224b7` |
| `founder-casual.jpg` | 2,680,522 | `2c38e1e97d7a44e444c2677fdb9f41c73aa593d75a0cb55096e27a54d6b41c44` |
| `item379-report.md` | this file | — |

## Open, both the Chair's

- F72 on the brief and on the delivery, once the two documents are attached.
- A professional headshot, if one exists.
