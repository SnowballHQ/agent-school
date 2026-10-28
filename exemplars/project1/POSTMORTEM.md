# Postmortem (this is the exemplar's RESULTS.md and the project's comparison of prediction to measurement)

Run: 24 postings, one pass, model calls 24, retries 0, schema failures 0. Scored on the 15 hand-labelled postings (`eval-v0.txt`).

## Predicted versus measured

| Prediction | I said | Measured |
|---|---|---|
| Cell accuracy on the 15-row sample | 85% | **88.6%** (93 of 105) |
| Meets my own bar (90% and zero confident-wrong deadlines) | expected to fail | **FAIL**, on both counts |
| Tokens per posting | about 850 | **524** average (about 380 in, 143 out) |
| Tokens for one hundred postings | about 85,000 | about **52,000** by extrapolation |
| Field that fails most | travel_support | **travel_support**, 11 of 15 (73%) |
| Confident-wrong deadlines | 1 | **2** |
| Schema failures on the first try | 0 or 1 | **0** (the retry path never ran, so it is untested) |

Per field: conference_name 100%, is_cfp 93%, event_start_date 93%, submission_deadline 87%, format 87%, audience_level 87%, travel_support 73%.

The two numbers I got right (accuracy within 4 points, the worst field) are the shallow ones. The cost I over-guessed by 60%, because I guessed the instructions would be longer than they were. The deadline count is the one that matters, and I was off by a factor of two in the wrong direction.

## The two confident-wrong deadlines, which are the real result

1. **`cfp-06`: the model did sums.** The posting says abstracts are due "six weeks before the event". The event is on 22 October. The model counted back and answered 10 September 2026, a date nobody wrote. It also happened to be two days before the posting itself was published, so the call had already closed. This is the exact failure the one-pager names.
2. **`cfp-16`: the model picked one of two.** The posting gives a full-paper deadline (20 November 2026) and an extended-abstract deadline (15 January 2027). The model chose January. A speaker with a full paper would have believed she had two extra months.

## The guard I built did not catch either one

The one-pager's design decision was: keep a date only if the quoted words appear in the posting. Both wrong dates came with a quote that really was in the posting ("Abstracts are due six weeks before the event." and "Extended abstract deadline: 15 January 2027."). The guard checked that the quote exists. It did not check that the date follows from the quote, and the model supplied honest evidence for a wrong conclusion. `outputs/guard.jsonl` was never created because the guard never fired once.

So the "must never happen" line did change a design decision, which satisfies the clinic, but the decision as built only prevents the invented-quote version of the mistake. What would work, and v1 should do:
- Make code check that the date, written in the posting's own format, appears inside the quote. "Six weeks before" contains no date, so 10 September fails and becomes null.
- Make the model return every candidate deadline it sees as a list, and let code choose null when there is more than one.

## Where the other misses came from

- **Prompt gaps I could have predicted.** I left the "two deadlines" and "range of levels" rules out of the v0 prompt, but they are in my labelling rules. The labels know something the prompt does not. That is the single most useful fact about v0: part of the gap between prompt and labels is my own spec not being passed on.
- **`cfp-23`, the unconference** (no advance submission at all). The model said it was a call for papers and filled in everything. I labelled it "not a CFP". That is a judgment I made, and someone else could label it the other way. All five of its wrong cells are one disagreement counted five times. Fix the label rule before fixing the agent.
- **`travel_support`.** Three of its four misses are the same cause: when only some people qualify (a grant for a student, for one under-represented group, "exceptions at the organisers' discretion") the model says `partial` and I say `none` or `unclear`. The schema has no way to say "only for some people", so that disagreement is partly the schema's fault.
- **`cfp-16` format.** The posting says virtual attendance is for registrants only and all presenters must attend on site. The model read "virtual option" and said hybrid. A careful human might too.

## Limits of this result

- I wrote the postings, wrote the labels, and wrote the prompt. The labels were fixed before the agent ran, but they come from the same head. A second person labelling the same 15 would probably differ on some cells (cfp-02, cfp-06, cfp-23 were close calls for me), and that disagreement ceiling, not the agent, may be what limits accuracy.
- Fifteen rows means one posting is 6.7 points of row accuracy. The 88.6% to 90% gap is less than one wrong cell on a different day. The confident-wrong count of 2 is the result I would trust.
- Nine postings were run but not labelled. Their outputs exist and are unchecked.
- The run is a single pass. The harness would want it run twice; `run-twice-diff.txt` shows it is. Run two cost nothing because finished postings are skipped.

## What to try differently

Label first, in a spreadsheet, with a second person if you can. Write down the rules as you hit disagreements and paste them into the prompt before you run. Then put your effort where the "must never happen" line points: build the check for it before you build anything else, and test the check itself on a posting that is designed to beat it.

## The one sentence that goes in your own file

I predicted one confident-wrong deadline and a 85% average; I got two and 88.6%, and my own guard missed both because I had checked that the evidence existed and not that it supported the answer.
