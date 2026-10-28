---
title: "Week 4: the model ladder, caching, and the cost curve"
access: free
---
# Week 4: the model ladder, caching, and the cost curve

Portfolio mission. Goes in your own repo. You already have an eval and a baseline from Week 3. This week you spend that ruler on cost.

**Start here if** you know your agent's accuracy but not what a thousand rows cost. Skip it if you already have a cost/accuracy table over three or more configurations, from logged tokens, with a working cache.

## The three ideas you need

1. **Models come in a ladder, and the top rung is rarely needed for every step.** A **model ladder** ranks models from small, fast and cheap to large, slow and expensive. Easy steps, such as "which of five labels fits?", can often step down without the score moving. Field note: "Why does every agent need a budget?"
2. **Caching means not paying twice for the same thing.** **Prompt caching** lets the provider reuse the unchanged start of your prompt, such as instructions and examples, at a discount. An **answer cache** is your own file storing the result for an input already processed. Field notes: "What is a context window, and what happens when it fills up?" and "What are tokens, and why does anyone count them?"
3. **A cost number without an accuracy number is a trap.** The honest report is a **cost/accuracy curve**: several configurations, each plotted by cost per thousand rows and held-back accuracy. Field notes: "How do you present numbers people can check?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result.

## The mission

Use the same `eval.py` and held-back rows from Week 3. Do not relabel or change the metric. Write `BRIEF.md` (including the line `Baseline: baseline`) and log choices in `DECISIONS.md`.

1. **Measure real cost** per thousand rows from the token counts on each call (`usage`, or your provider's equivalent), never from your estimate. Price it with the model's published price table, or with `total_cost_usd` on print mode (notional on a subscription). If neither fits, use relative units (cheapest model = 1) and say so in `DECISIONS.md`. Every model call appends a line to `calls.jsonl` with `row_id`, `tokens_in`, `tokens_out`, `cached_tokens`.
2. **Climb down the ladder.** At least three configurations in `ladder.csv`: `baseline` (your Week 3 setup), the same pipeline with a cheaper model for easy steps, and one mix of your own design, such as cheap first and the strong model only when it is unsure. Same held-back rows each time. Save each run's log as `runs/<name>.log`.
3. **Add caching.** Prompt caching for your fixed instructions and examples where your provider has it (print mode and the Anthropic API report `cache_*` fields in `usage`; if yours has none, say so in `DECISIONS.md`), plus an answer cache keyed on a hash of the input. A second run of unchanged rows makes zero model calls; changing one row's text bypasses the cache for that row only. The `Run:` line in `README.md` carries `--rows <path>`, where the path is a JSONL file with one object per row and an `id` field. The cache check edits the longest string field of the first row in a copy of that file.
4. **Reach the target:** cost per thousand rows at most half the baseline, with held-back accuracy within two percentage points of it.
5. **Write `MEMO.md`**, one page, for a person who will never read the code, under the headings `## What it does`, `## What it costs per month`, `## How good it is`, `## What could go wrong`, `## Recommendation`. Add `Best configuration: <name>` and `Target reached: yes|no`. Ask someone outside the course "would you pay for this?" and record `Reader answer: yes|no|maybe, <who>`; if nobody is available, write `Reader answer: none available`.
6. **If you cannot reach the target,** the mission still counts if your curve is honest and `MEMO.md` has a `## Why not` section saying why. Field note: "How do you say 'it didn't work'?"

## Deliverable and how it's checked

`BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `ladder.csv` (`name,models,cost_per_1k_rows,held_back_accuracy,rows`), `make_curve.py` and `curve.png`, `runs/`, `calls.jsonl`, the cached configuration, `MEMO.md`.

Two local feedback surfaces, and neither blocks the next mission: `/agent-school:check week4` and `/agent-school:defend`, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week4
- `ladder.csv` header is exactly `name,models,cost_per_1k_rows,held_back_accuracy,rows`; >=3 data rows; one row named `baseline`; cost and accuracy columns are numeric (accuracy is 0-100, e.g. `85`)
- every `name` in `ladder.csv` has a non-empty `runs/<name>.log`
- `python make_curve.py` exits 0 and `curve.png` has a newer modification time afterwards
- cache check: the README `Run:` line carries `--rows <path>` to a JSONL file (one object per row, each with an `id`); run it twice in a copy of the folder; `calls.jsonl` gains 0 lines during run 2
- single-row check: append text to the longest string field of the first row in the copy of the rows file and run again; every new `calls.jsonl` line has that one `row_id`, and there is >=1
- `MEMO.md` has the five headings above, <=500 words, `^Best configuration: ` naming a `name` in `ladder.csv`, `^Target reached: (yes|no)$`, and `^Reader answer: `
- if `Target reached: yes`: the best row's `cost_per_1k_rows` <= 0.5 * the baseline's and its `held_back_accuracy` >= baseline's minus 2.0
- if `Target reached: no`: `MEMO.md` has a `## Why not` section with >=2 non-empty lines
- `BRIEF.md` four sections; `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=2 entries
```

Examiner probes:
- Which step tolerated the cheapest model, and what is your evidence?
- How would the curve change on rows unlike your held-back set?
- What does "per month" assume about volume, and where did that number come from?
- Would the reader who said yes or no have changed your recommendation?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` first.

1. How many times cheaper will your cheapest configuration that holds accuracy be than the baseline?
2. Which step in your pipeline will tolerate the cheapest model, and which will not?
3. What percentage of your first rerun's cost will caching remove?

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 3-2` if tokens and cost are fuzzy. Run `/agent-school:notes 11-2` before you draw the curve.
- Notes: 6-2, 3-2, 3-3, 11-1, 11-2, 11-3.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
