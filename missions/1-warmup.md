---
title: "Warm-up: the job-watch agent"
access: free
---
# Warm-up: the job-watch agent

Free. One evening. Not portfolio; this one is for you.

**Start here if** you have called a model from code but never built something that must be safe to run twice. Skip it if you already have an agent with a memory file whose second run changes nothing, and you can show the diff.

## The three ideas you need

1. **An agent is a goal, some tools and a loop.** A **tool** is a function the model may ask your program to run, such as "search the job board." The **loop** is: look, decide, act, look again. Field note: "What turns a chatbot into an agent?"
2. **Your agent talks to the board through an MCP server.** An **MCP server** is a program that publishes a list of tools in a standard way. Deployed publishes one at `https://deployed.so/mcp`. The tool descriptions are what your agent reads to decide what to do, so read them the way it will. Field note: "What is an API, really?"
3. **Run it twice, and nothing may change.** Something **idempotent** leaves the world in the same state whether you run it once or twice. Your agent needs a memory of what it has seen, and a plain file is enough. Field notes: "What happens when you run it twice?" and "Where does an agent keep its state?"

## Who builds

You do not type the code. You write the brief and the prediction; your agent builds; you read the trace and the result.

## The mission

Direct your agent to build a watch on the Deployed board for a search you care about, reporting only what changed since it last looked.

1. **Read the tools.** Have your agent connect to the MCP server, list the tools, save the list to `tools.txt`, and read every description, including any rule about location or country that your search must obey.
2. **Choose a narrow watch**, one search such as role family plus seniority plus a location rule, saved in `watch.json`. The search returns 50 postings a page. If your watch cannot be read fully, narrow it; never truncate it, because postings that fall off the end look "gone".
3. **Write `BRIEF.md`**: what to build, inputs and outputs, what must never happen, how you will check it. It must say that the key is the posting's `slug`, and that **code does the diffing, not the model**. A watch built right costs zero tokens when nothing changed. Say where the model credentials live (an environment variable, never committed).
4. **Memory file `state.json`:** `{"meta": {"fetched": N, "complete": true}, "postings": {"<slug>": {"title", "first_seen", "last_seen", "gone_at"}}}`. A posting that vanishes keeps its key and gets a `gone_at` timestamp, reported once as `gone`. If it reappears, `gone_at` clears and it is reported as `returned`. Compare by key, never by list position. Write the file only when something changed.
5. **Output format**, one line per change: `new: <slug> | <title>`, `gone: <slug> | <title>`, `returned: <slug> | <title>`, or the single line `nothing new`.
6. **Run twice.** The second run must print exactly `nothing new` and leave `state.json` byte-identical. The two outputs differ by design; only the memory file is diffed.
7. **Stage a change.** Edit a copy of the memory file to delete one key and run again with `--state <copy>`. The agent must report exactly that one posting as `new`. The check does this itself: after run 2 it deletes the alphabetically first key from a copy of `state.json` and expects exactly one `new: <slug>` line.
8. **Write the README**: `Watch:` (what you watch), `Run:` (the command, which must accept `--state <path>`), `Credentials:` (where the key lives, or `none needed`). Start `DECISIONS.md`.

## Deliverable and how it's checked

A folder with `BRIEF.md`, `PREDICTION.md`, `DECISIONS.md`, `README.md`, `watch.json`, `tools.txt`, the agent, `state.json`. If the model is called at all, each call appends one line to `usage.jsonl` with `tokens_in` and `tokens_out` from `usage` (or your provider's equivalent).

Two local feedback surfaces, and neither blocks the next mission: `/agent-school:check warmup` (below) and `/agent-school:defend`, the examiner, which writes feedback on your reasoning into `COURSE_PROGRESS.md`.

```
Local check contract: /agent-school:check warmup
- `README.md` has lines starting `Watch: `, `Run: ` and `Credentials: `; the `Run:` command contains `--state`
- `tools.txt` exists and is non-empty; `watch.json` parses as JSON
- `state.json` parses; `meta.complete` is true; `meta.fetched` >= 1; `postings` has >=1 key; every value has the keys title, first_seen, last_seen, gone_at
- run the `Run:` command (run 1, on a fresh copy of the folder with `state.json` removed; it needs network access to the board): exit 0
- run it again (run 2): exit 0, stdout trimmed equals `nothing new`, sha256 of `state.json` equals its value before run 2
- `usage.jsonl` line count is unchanged across run 2 (a missing file counts as 0)
- staged change (after run 2): delete the alphabetically first key from a COPY of `state.json`, run with `--state <copy>`: stdout has exactly one line starting `new: <that slug>`
- `BRIEF.md` has sections `## What to build`, `## Inputs and outputs`, `## Must never happen`, `## Checks`, each >=1 non-empty line, and mentions `slug`
- `PREDICTION.md` has `## Predictions` (3 numbered lines) and `## The gap` (>=1 non-empty line)
- `DECISIONS.md` has >=1 entry (`### D1:` with `Decision:`, `Alternatives:`, `Why:`, `Evidence that would change it:`)
- no file matches `sk-[A-Za-z0-9_-]{20,}`
```

Examiner probes:
- Why this key, and what happens to your memory when a posting disappears and returns?
- Which part does the model decide, and why not the diff? What did your second run cost?
- How narrow is your watch, and how do you know you read it all?
- What did the staged change show that the plain second run could not?

## Predict before you build

Write these in `PREDICTION.md` first, under `## Predictions`.

1. How many postings will your search return today?
2. What will the first full check cost in tokens, and what will the second cost?
3. After you delete one key, how many `new:` lines will you see?

Then add `## The gap`.

## When you're stuck

- Run `/agent-school:mission` and the mentor resumes you at the right step.
- Run `/agent-school:notes 6-4` if the second run is not empty. Run `/agent-school:notes 7-1` if your memory file got messy. Run `/agent-school:notes 7-2` if the model is doing the diffing. Run `/agent-school:notes 6-2` before you point any loop at something that bills.
- Run `/agent-school:defend` when you think you are done, even if the check fails; the feedback is the point.
