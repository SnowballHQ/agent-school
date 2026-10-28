---
title: "Project 1: find the problem, then build extraction v0"
access: free
---
# Project 1: find the problem, then build extraction v0

Portfolio mission. Goes in your own repo. Two parts: discovery first, then a first agent.

**Start here if** you have run a model on some documents but never written down what "correct" means before building. Skip it if you already have a one-pager with a runnable test and a schema-validated extraction run, and can show both.

## The three ideas you need

1. **A requirement is something a person can confirm and a test can check.** A **requirement one-pager** has six headings: the problem, the manual process today, inputs and outputs, what "correct" means as a runnable test, what must never happen, and the budget. Field notes: 2-1 and 2-2.
2. **One sentence about what must never happen can reshape the system.** Name the expensive mistake in plain words, then design around it. 
3. **Make the model answer in a schema.** A **schema** lists the fields allowed, the type of each, and the legal values. **JSON** is plain text with labeled values in curly brackets. "Valid" means the answer matches the schema exactly; anything else is a failure to handle, never something to pass along. Field notes: 4-1 and 4-2.

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result. For this project the brief is `ONE_PAGER.md`.

## The mission

**Part A, discovery.**

1. Pick a vertical you know. In `DISCOVERY.md` write three numbers from your own knowledge or public sources, each naming its source: volume (items per period), frequency (how often the work happens), cost of the manual way (minutes or money per item). Then conclude `worth` or `not worth`. "Not worth automating" is a valid outcome; if you reach it, say why, and do Part B on a stand-in domain such as job postings so you can still practise.
2. Write `ONE_PAGER.md` under six headings. Heading four must be a runnable test, such as "ninety of a hundred reviewed rows match a human's answer". Heading five is the thing that must never happen, in a concrete example. It has to change at least one design decision you can point to in `DECISIONS.md`, and you must test it (see Part B).
3. Design the schema (`schema.json`) with fixed option lists wherever a field could drift. Decide multi-value cases up front ("intermediate to advanced": a list, a range, or the lower bound?) and log it in `DECISIONS.md`.
4. Write `PREDICTION.md` after the schema is final and before any run.

**Part B, extraction agent v0.** Direct your agent to build an agent that reads one document from `postings/` and writes `outputs/<id>.json` matching `schema.json`. Run it on at least twenty. Handle a non-matching answer by retrying once, then recording the failure in `failures.jsonl` (`id`, `reason`), never by passing it on. Every model call appends a line to `usage.jsonl` with `tokens_in`, `tokens_out`. Then:

- **Test the retry path.** Feed the agent one deliberately malformed answer and save the result in `RETRY_TEST.txt` as the lines `attempts: 2` and `result: valid` or `result: recorded failure`.
- **Test your guard.** Build one posting meant to beat your own guard (a quote that is real but the answer wrong) in `adversarial/`, run it, and record `GUARD_TEST.md` with `posting: adversarial/<file>` and `result: caught` or `result: missed`. A first guard that only checks the quoted evidence exists will miss a confident wrong answer whose quote is real.
- **Label 15 rows yourself** in `labels.csv` (`id` plus one column per schema field) before the run, without looking at output.

## Deliverable and how it's checked

`DISCOVERY.md`, `ONE_PAGER.md`, `DECISIONS.md`, `PREDICTION.md`, `schema.json`, the agent, `postings/`, `outputs/`, `failures.jsonl`, `usage.jsonl`, `labels.csv`, `RETRY_TEST.txt`, `GUARD_TEST.md`, `adversarial/`, `RESULTS.md`.

`RESULTS.md` has the lines `Accuracy on reviewed sample: X of 15`, `Tokens in:`, `Tokens out:` and `Cost:` (from `usage`, the only honest cost, since hidden reasoning tokens can double an estimate), plus `## The gap` against each prediction.

**The v0 check is format-only and says so**: it proves the files parse and validate, not that the dates are right. Accuracy becomes your Week 3 eval. Two local feedback surfaces, and neither blocks you: `/agent-school:check project1` and `/agent-school:defend`, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check project1
- `DISCOVERY.md` has lines matching `^Volume: .+ \| Source: .+`, `^Frequency: .+ \| Source: .+`, `^Cost of the manual way: .+ \| Source: .+`, and `^Conclusion: (worth|not worth)$`
- `ONE_PAGER.md` has exactly six `## ` headings, in order: `The problem`, `The manual process today`, `Inputs and outputs`, `What correct means`, `What must never happen`, `The budget`; each has >=1 non-empty line
- `schema.json` parses and has `type`, `properties` and `required`
- `postings/` holds >=20 files; `outputs/*.json` count >= 20 minus the number of lines in `failures.jsonl`; every output parses and validates against `schema.json`
- every id in `postings/` has either `outputs/<id>.json` or a `failures.jsonl` line with that `id`
- `usage.jsonl` line count >= `outputs/*.json` count; each line parses with integer `tokens_in`, `tokens_out`
- `RETRY_TEST.txt` has lines `^attempts: 2$` and `^result: (valid|recorded failure)$`
- `GUARD_TEST.md` has `^posting: adversarial/\S+` naming an existing file and `^result: (caught|missed)$`
- `labels.csv` has >=15 rows; `id` values exist in `postings/`; header holds every schema field
- `RESULTS.md` has `^Accuracy on reviewed sample: \d+ of 15$`, `^Tokens in: \d+`, `^Tokens out: \d+`, `^Cost: ` and a `## The gap` section with >=1 non-empty line
- `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap`
- `DECISIONS.md` has >=2 entries; one mentions `multi-value`, one mentions `must-never`
- no file matches `sk-[A-Za-z0-9_-]{20,}`
```

Examiner probes:
- Where did each of your three numbers come from, and what would make you conclude "not worth"?
- Which design decision did "must never happen" change, and what did your adversarial posting show?
- How did you label the 15 rows, and could the agent's answers have influenced you?
- Which field will fail most often now that the schema is final, and why?
- Were the labels written before you saw the agent's output? Show me the commit order.

## Predict before you build

1. What accuracy will v0 reach on your 15 reviewed rows?
2. What will one posting cost in tokens, and what will one hundred cost?
3. Which field will fail most often, and why?

## When you're stuck

- Run `/agent-school:mission` to resume. Run `/agent-school:notes 2-2` if your one-pager has blanks, or `/agent-school:notes 4-2` if outputs keep breaking the schema.
- Notes: 2-1, 2-2, 1-3, 4-1, 4-2, 6-2.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
