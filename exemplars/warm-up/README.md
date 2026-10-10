# Job-watch agent (warm-up exemplar)

Watches the Deployed remote-jobs board for one search and reports only what is new or gone since the last check.

**What it watches** (`watch.json`): senior machine-learning and AI roles, remote or open to workers in India, newest first. Today that is 100 postings.

**Run it**

    export LLM_API_KEY=...  LLM_BASE_URL=...  LLM_MODEL=...   # your own; only needed when something is new
    python3 watch.py              # one check
    python3 watch.py --tools      # list the board's tools and read their descriptions
    python3 watch.py --state x.json   # use a different memory file

Run it twice. The second run prints `nothing new` and does not touch `state.json`.

**Read in this order**

1. `PREDICTION.md`, written before the runs.
2. `tools.txt`, the board's tool list as the agent sees it.
3. `watch.py`, the whole agent, standard library only.
4. `state.json`: the memory. Keyed by posting id, sorted, written only on change.
5. `runs/run1.out` and `runs/run2.out`: the first and second check.
6. `diff.txt`: the run-twice check, empty as required.
7. `runs/run3-staged.out`: a staged change, to show the agent can see one.
8. `trace/`: the real decision trace, one folder per run (`events.jsonl` has each board call; `session-warmup.jsonl` has the model call and its cost). The second run has no model call at all, which is why its cost is 0.
9. `attempt1-silent-summary/`: the first attempt, which cost 2,938 tokens and printed a blank. Kept on purpose.
10. `POSTMORTEM.md`.

Posting titles, skill tags and company names are copied verbatim from the live board on 10 October 2026; they may mention products of other companies. Nothing here is edited except the model's name in the trace, replaced with `<model-id>`.
