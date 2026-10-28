---
title: "Week 0: set up, make your first call, read a trace"
access: free
---
# Week 0: set up, make your first call, read a trace

Free. One sitting, about two hours. No portfolio value; this one makes everything after it possible.

**Start here if** you have never called a model from code or opened a trace. Skip it if you already have a script that calls a model and prints token counts, and you can show the log of a run.

## The three ideas you need

You do not have to have read anything first. These three are enough to start.

1. **A model predicts text, and you pay for it by the token.** A **model** is a program that reads text and writes the most likely continuation. A **token** is a small chunk of text, roughly three quarters of a word, and it is the unit you are measured and billed in. Field notes: 3-1 and 3-2.
2. **An API is a contract for asking a program to do something.** An **API** is a fixed way to send a request to another program and get a predictable reply. Your first call is one request out, one reply back. Field note: "What is an API, really?"
3. **A trace is the record of what happened.** A **trace** logs every step of a run: what was sent, what came back, what it cost. Models give different answers each time, so you read the trace instead of trusting memory. Field note: "Why does the same question get different answers?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result. Your agent is the mentor in this plugin.

## Choose where your agent's model runs

Everything you build later calls a model, so you choose one now and record it. Three options:

- **(a) Claude Code print mode, on your subscription.** `claude -p --output-format json "<prompt>"` returns JSON with `result` (the reply), `usage` (`input_tokens`, `output_tokens`, `cache_*`) and `total_cost_usd`. No API key needed.
- **(b) An Anthropic API key** from console.anthropic.com. Prepaid; the whole course costs a few dollars. Never commit the key; keep it in an environment variable.
- **(c) Any other provider you already have.** Use whatever token counts its replies carry.

Write one line in `COURSE_PROGRESS.md`: `Model choice: a`, `b` or `c`, then a dash and the details. From now on, "tokens" means the numbers in `usage` (or your provider's equivalent), never your estimate.

## The mission

1. **Set up.** Install the plugin, open a fresh folder, run `/agent-school:setup`, and confirm `.course/` exists with `ls -a`. Ask your agent to create `hello.txt`; if it does, setup is done.
2. **Brief your agent, first call.** Write `BRIEF.md`: what to build (a script `ask.*` that sends one question to your chosen model and prints reply and tokens in and out), inputs and outputs, what must never happen (the key written into a file), and how you will check it. Then direct your agent to write the script. Run the same question three times, then a changed question once: four runs. Notice that the three same-question replies differ, and that the token counts differ too.
3. **Read a trace.** Your session's trace is in `.course/trace/`. Find five things and write one line each in `TRACE_NOTES.md`: your first request, the model's reply, the token counts, the moment the script ran, and the stop or finish reason (why the model stopped). Start `DECISIONS.md` with the model choice.

## Deliverable and how it's checked

Your folder holds `BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `hello.txt`, the script, `runs.txt`, `replies/run-1.txt` to `run-4.txt`, `TRACE_NOTES.md`, and the `Model choice:` line.

A decision-log entry is `### D<n>: <title>` followed by lines `Decision:`, `Alternatives:`, `Why:` and `Evidence that would change it:`. All later missions use this format.

Two local feedback surfaces, and neither blocks you. `/agent-school:check week0` runs deterministic checks (below). `/agent-school:defend` is the examiner: it asks you to defend your brief, prediction, decisions and results, and writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check week0
- `.course/` exists; `.course/trace/` holds >=1 non-empty file; every `.jsonl` line there parses as JSON
- `hello.txt` exists and is non-empty
- `COURSE_PROGRESS.md` has a line matching `^Model choice: (a|b|c)\b`
- a file matching `ask.*` exists; `replies/run-1.txt` ... `replies/run-4.txt` exist and are non-empty
- `runs.txt` has exactly 4 lines matching `^run [1-4] \| q=[AB] \| in=\d+ \| out=\d+ \| `; runs 1-3 have q=A, run 4 has q=B
- `TRACE_NOTES.md` has exactly 5 non-empty lines matching `^[1-5]\. `; each contains a path starting `.course/trace/` that exists
- `BRIEF.md` has sections `## What to build`, `## Inputs and outputs`, `## Must never happen`, `## Checks`, each with >=1 non-empty line
- `PREDICTION.md` has a `## Predictions` section with 3 numbered lines and a `## The gap` section with >=1 non-empty line
- `DECISIONS.md` has >=1 entry `### D1:` containing the four labelled lines, each non-empty
- no file in the folder matches `sk-[A-Za-z0-9_-]{20,}`
```

Examiner probes:
- Which option did you choose, and what would make you switch?
- Why did your "must never happen" line say what it says, and how did you check it?
- Show me where in the trace the stop reason is. What would a different value mean?
- Why did your prediction differ from the measured token count?

## Predict before you build

Write these in `PREDICTION.md` under `## Predictions` before you run anything. Wrong numbers cost nothing.

1. How many tokens will your one question use, in and out together?
2. Of the three same-question runs, how many replies will be word-for-word identical (0 to 3)?
3. Will the changed question use more or fewer tokens than the first, and by roughly how many?

After the fourth run, add `## The gap`: one sentence per prediction on what happened.

## When you're stuck

- Run `/agent-school:mission` and your mentor finds which step you are on and continues.
- Run `/agent-school:notes 3-2` (or any note number) to have the mentor re-teach that note against what is on your screen. Notes: 3-1, 3-2, 3-4, 8-1.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
