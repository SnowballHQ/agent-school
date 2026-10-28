---
title: "Week 2: the loop, two tools, and a budget in code"
access: free
---
# Week 2: the loop, two tools, and a budget in code

Portfolio mission. Goes in your own repo. You take your Project 1 extraction agent from "it produced JSON" to "it is a real agent with walls and a number on record."

**Start here if** you can describe what a tool call is but have not capped one. Skip it if you have already built a tool-calling loop with hard budget caps and can show the trace.

## The three ideas you need

1. **The agent loop is: model decides, your code acts, the result goes back.** The model never runs anything. It asks for a **tool call**, a named function plus arguments, and your program decides whether to run it. The loop ends when the model says it is done or when your code stops it. Field note: "What turns a chatbot into an agent?"
2. **A tool is a spec you write by hand.** Each tool has a name, a plain-words description, and an **input schema** (arguments allowed, types, legal values). The model reads your description to decide when to call it, so a vague description makes a confused agent. Field note: "What should the model not decide?"
3. **A budget is a limit enforced by code, never by asking nicely.** A **budget** caps something you can count: model calls, tokens, dollars. Your code checks it before every call and stops the loop when it is spent. Field note: "Why does every agent need a budget?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result.

## The mission

Rebuild your Project 1 extraction as a real loop, same input and same schema. Write `BRIEF.md` first (what to build, inputs and outputs, what must never happen, the checks), then direct your agent. Log choices in `DECISIONS.md`.

1. **Exactly two tools, specified by hand** in `tools.json`: `read_document(doc_id)` returns the text, `submit_record(json)` accepts the final answer. Each has `name`, `description`, `input_schema`. A row cannot finish without `submit_record`.
2. **Validation walls.** Code checks every tool call before running it: unknown tool, missing or extra arguments, wrong types, a `doc_id` that does not exist. A bad call returns a plain error to the model and counts against a retry limit of two per row. After that the row is recorded as failed, never guessed.
3. **Budget caps in code**, in `config.json`: `max_calls_per_row`, `max_total_tokens`, `max_total_spend_usd`. Tokens come from `usage` (or your provider's equivalent); on a subscription, spend is `total_cost_usd` as notional. Before the next call can start, every model call appends one line to `spend.jsonl`: `time`, `row_id`, `tokens_in`, `tokens_out`, `running_total` (tokens). When a cap is hit the run stops and its last stdout line is `stopped: <interrupted|cap:NAME> total_tokens=N`.
4. **Hand-label fifteen rows** in `labels.csv` (`id` plus one column per schema field), rows you did not use to design the schema, before you see agent output. Reuse your Project 1 labels only if they fit the current schema, and say so.
5. **`score.py`** compares output to `labels.csv` field by field and prints the share correct overall and per field.
6. **Save the trace of one full row** as `trace_row.jsonl`, one JSON per line with `event` (`tool_call`, `tool_result`, `model_reply`) and `tool`.

README must carry `Run:` (accepting `--config <path>`; by default it processes all rows and must take at least 10 seconds, so the kill check can interrupt it mid-run) and `Test:` (a command that exits 0 and prints one `ok: <wall>` line per wall).

## Deliverable and how it's checked

`BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `tools.json`, the agent, `config.json`, `spend.jsonl`, `labels.csv`, `score.py`, `trace_row.jsonl`, `README.md`, and `WEEK2.md` with the lines `Accuracy: NN%` and `Error estimate: ±N points` (how wide you think the error is on fifteen labels; Week 3 tests that), plus the two kill counts.

Two local feedback surfaces, and neither blocks you: `/agent-school:check week2` and `/agent-school:defend`, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week2
- `tools.json` parses to an array of exactly 2 objects, each with non-empty `name`, `description` and an `input_schema` object; one name is `submit_record`
- `config.json` has numeric `max_calls_per_row`, `max_total_tokens`, `max_total_spend_usd`
- `trace_row.jsonl` has >=1 `tool_call` for `read_document`, >=1 for `submit_record`, each followed later by a `tool_result` line
- `Test:` command exits 0 and prints lines `ok: unknown_tool`, `ok: missing_args`, `ok: wrong_type`, `ok: bad_doc_id`, `ok: retry_limit`
- kill check: start `Run:` as written (all rows by default; it must still be running, >=10 s, when the check interrupts it), wait until `spend.jsonl` has >=1 line, send SIGINT; `wc -l spend.jsonl` read twice 10 s apart is equal; last stdout line matches `^stopped: (interrupted|cap:\w+) total_tokens=\d+$` and its number equals the last line's `running_total`
- cap check: `Run: --config <copy with max_total_tokens=50>` exits and its last line is `stopped: cap:max_total_tokens total_tokens=N`
- every `spend.jsonl` line parses with keys `time,row_id,tokens_in,tokens_out,running_total`
- `labels.csv` has >=15 rows and a header holding `id` plus every schema field
- `python score.py` exits 0 and prints a line matching `^overall: \d+(\.\d+)?%` and one `^field <name>: \d+(\.\d+)?%` per schema field; a second run prints the same `overall:` line
- `WEEK2.md` has `^Accuracy: \d+(\.\d+)?%`, `^Error estimate: ±\d+`, and `^Kill check: lines before=\d+ after=\d+$` with equal numbers
- `BRIEF.md` four sections; `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`; `DECISIONS.md` has >=1 entry
```

Examiner probes:
- Which wall fired most often, and did that match your prediction?
- What stops the loop if the model never calls `submit_record`?
- How far can you trust fifteen labels, and how did you choose your error estimate?
- What did you decide the model must not decide?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` first.

1. How many model calls will an average row take now, versus your single-call Project 1?
2. Which wall will fire most often in the first run?
3. Your accuracy on the fifteen rows, and which single field will be worst.

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 6-1` if the loop never calls a tool. Run `/agent-school:notes 6-2` if you are unsure what to cap.
- Notes: 6-1, 6-2, 7-2, 4-2, 6-5.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
