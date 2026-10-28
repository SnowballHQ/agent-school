---
title: "Week 5: state, kill -9, and the day the data changed"
access: free
---
# Week 5: state, kill -9, and the day the data changed

Portfolio mission. Goes in your own repo. Two things go wrong in production that never go wrong in a demo: the machine dies mid-run, and the data stops looking the way it did. This week you survive both.

**Start here if** your agent restarts from row one after a crash. Skip it if you already have a checkpointed run that survives `kill -9` with zero duplicate ids, and a guard with a test.

## The three ideas you need

1. **State is whatever your agent needs to remember between steps and between runs.** **Durable execution** means progress is written to disk after each unit of work, so a restart continues instead of beginning again. A **checkpoint** is one such written record. Field notes: "Where does an agent keep its state?" and "What happens when you run it twice?"
2. **Resuming must be safe to repeat.** A process can die mid-write, so write to a temporary file and rename it; a checkpoint is then whole or absent. Key every row by its id so reprocessing never creates a duplicate. Field note: "How should a system fail?"
3. **Real data changes without telling you.** A column is renamed, a date format switches, blanks appear: **schema churn**. The model keeps answering confidently, so the only alarm is your eval. Field notes: "Why is real-world data always messier than the demo data?" and "What breaks when two systems quietly disagree?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result.

## The mission

Take your best Week 4 configuration. Write `BRIEF.md` (what must never happen: a row paid for twice, a half-written checkpoint) and log choices in `DECISIONS.md`.

1. **Add checkpointing.** After every row, the agent appends the finished record to `outputs.jsonl` (one JSON per line with `id`) and atomically rewrites `checkpoint.json` (`rows_done`, `spend`, `updated_at`). A run reads the checkpoint and skips finished rows. Only `--fresh` deletes it. Every model call still appends to `calls.jsonl` with `row_id`.
2. **Prove it with `kill -9`.** Start a run on at least forty rows, send `kill -9 <pid>` at about half, start again. The `Run:` line in `README.md` carries `--rows <path>`, a JSONL file with one object per row and an `id` field, and the run must process at least 40 rows at 0.1 s or more each, so the check can catch it mid-run. Save in `RESUME.md`: `Rows before kill: N`, `Rows after resume: N`, `Duplicate ids: 0`, `Second-run model calls: N`.
3. **Keep your eval running.** Run your Week 3 eval each working day this week and append the held-back number to `eval_log.csv` (`date,held_back_accuracy,data_version`), with `data_version` set to `stable`. Three different dates at least; this habit is the actual mission.
4. **Cause a churn.** Real data may change under you this week; if you notice it, log it. Whether or not it does, make your own: copy a few rows into `rows_churned/` and rename a field or change a date format. Your eval must be able to read them. Run it and log the number with `data_version` `churned`. Predict the drop first.
5. **Respond.** `CHURN_REPORT.md`: `Churn kind: real|self-made`, `Before: NN%`, `After: NN%`, `After fix: NN%`, then plain words for the rows that fail, the root cause and the fix. Add a **guard** at the edge of your program that flags input no longer matching the expected shape before the model sees it. `Test:` in `README.md` runs it. Log the fixed run as `fixed`.

## Deliverable and how it's checked

`BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, the checkpointing agent, `RESUME.md`, `eval_log.csv`, `rows_churned/`, `CHURN_REPORT.md`, the guard with its test. The check is behaviour except for the report text. Two local feedback surfaces, and neither blocks the next mission: `/agent-school:check week5` and `/agent-school:defend`, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week5
- kill check, in a copy of the folder: the `Run:` line carries `--rows <path>` to a JSONL file of >=40 rows, one object per row with an `id`, each taking >=0.1 s; start it with `--fresh`; when `outputs.jsonl` has >= half the rows send SIGKILL; `checkpoint.json` parses afterwards and `rows_done` <= the lines in `outputs.jsonl`
- restart the same `Run:` command to completion: ids in `outputs.jsonl` equal the `id` values in the rows file exactly, with no duplicates (`jq -r .id outputs.jsonl | sort | uniq -d` prints nothing)
- after restart, no `row_id` in the new `calls.jsonl` lines is an id that was already in `outputs.jsonl` at kill time
- no file named `checkpoint.json.tmp` or `*.tmp` remains after completion
- `RESUME.md` has `^Rows before kill: \d+$`, `^Rows after resume: \d+$`, `^Duplicate ids: 0$`, `^Second-run model calls: \d+$`
- `eval_log.csv` header is `date,held_back_accuracy,data_version` (accuracy 0-100); >=3 `stable` rows with >=3 distinct ISO dates; >=1 `churned` row whose accuracy is lower than the last `stable` row before it; >=1 `fixed` row
- `CHURN_REPORT.md` has `^Churn kind: (real|self-made)$`, and `Before:`, `After:`, `After fix:` percentages (0-100) equal to the last `stable`, the `churned` and the `fixed` rows of `eval_log.csv`
- guard test: `Test:` exits 0 and prints `ok: guard accepts old shape` and `ok: guard rejects changed shape`; `rows_churned/` is non-empty
- `BRIEF.md` four sections; `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=2 entries
```

Examiner probes:
- What exactly happens if the kill lands during a checkpoint write?
- How did your eval notice the churn, and how many days would a real one have gone unseen?
- Is your guard checking shape only, or also meaning? What would it miss?
- Which row, if reprocessed, would cost the most?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` first.

1. If you kill at the halfway point, how many rows will be reprocessed after resume?
2. How much will held-back accuracy drop when the data changes, and which field falls first?
3. How many days would a real churn go unnoticed by your eval?

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 7-1` if your checkpoint is messy. Run `/agent-school:notes 8-2` if the data looks wrong and you do not know where to start.
- Notes: 7-1, 6-4, 9-2, 8-2, 8-3, 10-1, 10-2.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
