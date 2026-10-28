# Job-watch agent (warm-up exemplar)

> Rebuilt to the 2026-10-28 contract. Real and kept: the 2026-10-10 live runs, traces, postings, token counts, the first attempt and `POSTMORTEM.md`. Replayed: `watch.py --replay` serves the saved board pages in `board_saved.json` (rebuilt from the saved memory file: slug, title and company only) so the run works offline; the model is not called. Changed on purpose: output is now `new:/gone:/returned:` lines, `state.json` has the `meta`/`postings` shape, and three slugs containing `task-auditor` are written `task_auditor` (the course's secret scan treats `sk-` plus 20 characters as a key). `runs/`, `trace/` and `diff-live-run.txt` are the original live evidence in the old format; the old watcher is `runs/watch-live-2026-10-10.py`.

Watches the Deployed remote-jobs board for one search and reports only what is new or gone since the last check.

Watch: senior machine-learning and AI roles on the Deployed board, remote or open to workers in India, newest first (`watch.json`). Today that is 100 postings.
Run: `python3 watch.py --replay board_saved.json --state state.json`
Credentials: none needed for the replay run; only `--summarise` on the live board needs LLM_API_KEY, LLM_BASE_URL and LLM_MODEL (your own, in environment variables, never in a file).

Other ways to run it:

    python3 watch.py --state state.json     # one live check of the board
    python3 watch.py --tools                # list the board's tools and read their descriptions
    python3 watch.py --summarise --state state.json   # live check plus a model verdict per new posting; appends usage.jsonl

Run it twice. The second run prints `nothing new` and does not touch `state.json`.

**Read in this order**

0. `BRIEF.md`, `DECISIONS.md`, `COURSE_PROGRESS.md` (Model choice: b, an API key).
1. `PREDICTION.md`, written before the runs.
2. `tools.txt`, the board's tool list as the agent sees it.
3. `watch.py`, the whole agent, standard library only.
4. `state.json`: the memory. Keyed by posting slug, sorted, written only on change. `usage.jsonl`: the three real model calls.
5. `runs/run1.out` and `runs/run2.out`: the first and second check.
6. `diff-live-run.txt`: the run-twice check on the live run, empty as required.
7. `runs/run3-staged.out`: a staged change, to show the agent can see one.
8. `trace/`: the real decision trace, one folder per run (`events.jsonl` has each board call; `session-warmup.jsonl` has the model call and its cost). The second run has no model call at all, which is why its cost is 0.
9. `attempt1-silent-summary/`: the first attempt, which cost 2,938 tokens and printed a blank. Kept on purpose.
10. `POSTMORTEM.md`.

Posting titles, skill tags and company names are copied verbatim from the live board on 10 October 2026; they may mention products of other companies. Nothing here is edited except the model's name in the trace, replaced with `<model-id>`.
