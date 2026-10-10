# Postmortem

## Predicted versus actual

| Prediction | I said | Actual |
|---|---|---|
| Postings returned today | about 60 | **100** (two pages of 50) |
| Tokens, first check | about 4,500 | **2,048** (938 in, 1,110 out) in the final run; 2,938 in the first attempt, see below |
| Tokens, second check | 0 | **0** |
| New postings between runs | 0 new, 0 gone | 0 new, 0 gone |
| Second run leaves the memory file unchanged | yes | **yes**: `diff.txt` is empty, both files hash to `ee1988fc...`, and the file's modified time did not move |

I was 40% low on the count and 55% high on the tokens. The two misses have the same cause: I guessed the pool, not the thing the pool feeds. More postings should have meant more tokens; instead the check summarises at most 25 new postings, so the cost has a ceiling that has nothing to do with how many the board returns.

Between two runs about 15 seconds apart nothing changed on the board, as predicted. That is a weak result: it tests that "no change" is reported as no change, and nothing else. So `runs/run3-staged.out` stages a change on purpose (one posting deleted from memory, one invented posting added) and shows the agent report exactly 1 new and 1 gone, and then report nothing on the repeat. That invented posting is labelled `example` in the file.

## What went wrong, in the order it happened

1. **A run that cost 2,938 tokens and printed no summary.** `attempt1-silent-summary/` holds it. The summary step was allowed 2,000 tokens of output. The model used all 2,000 on hidden thinking and wrote nothing, and the reply said it stopped because it ran out of room. My code printed the empty text and carried on, so the alert looked complete: a list of 25 titles, a blank space where the verdicts should be, and a normal-looking cost line. Two fixes, both in `watch.py`: more room (6,000), and the check on why the model stopped. If it did not stop because it finished, the alert now says `[summary unavailable ...]` out loud. The lesson is in the trace, not the output: only the reply's stop reason showed it.
2. **An unrecorded development run.** Before the attempt in the folder I ran the agent once to see its output and then deleted that run's files to renumber the list. That run is not in the trace. It cost about 1,800 tokens. The totals in this exemplar are therefore about 7,000 tokens, not the 2,235 of the final runs.
3. **The watch was too loose.** Of the first 25 postings, 8 are freelance "AI trainer project" gigs and 2 are architect roles, which the model correctly marked SKIP. The board's search tool has a switch to hide gig work (`exclude_gig`), named in its own description; I did not read the description the way my agent would, which is what step 1 of the brief asks for. The next version of `watch.json` should set it. The model also marked one "Manager (Individual Contributor)" posting WORTH A LOOK against my stated "not people management", a small miss that nobody would catch without reading the reasons.
4. **Not done, and should be.** The board's reply carries a `total` count with every page. I never checked that what I collected matched it. The watch happened to be exactly 100, which looks like a limit but is not (a wider search returned 191 across four pages). I only know that because I probed it after the fact.

## What the design got right (and why it is not luck)

- Postings are compared by their id (`slug`), never by position. The board sorts "newest first", and a position-based comparison would report every posting as changed the moment one new posting arrived at the top.
- The memory file is written only when something changed, with sorted keys and fixed indentation. That is why the file did not even change its modified time.
- A failed fetch, or a watch too broad to read fully, stops the run before touching memory. Otherwise a half-read list would mark everything unread as "gone".
- The code decides what is new. The model only writes the summary. When the summary failed (attempt 1), the memory was still correct.
- I did not put a date filter such as "posted in the last 30 days" in the watch. A window that moves would push postings out of the results as they age and report them "gone" when they are only old.

## The one sentence that goes in your own file

I predicted 60 postings and 4,500 tokens and saw 100 and 2,048; my real miss was not the numbers but that the first version printed a blank where the answer should be and looked fine.
