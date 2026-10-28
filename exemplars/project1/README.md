# Project 1 exemplar: conference call-for-papers extraction v0

> Rebuilt to the 2026-10-28 contract. Real and kept: the 24 postings, the 15 hand labels, the real run (outputs, trace, token counts), the prediction numbers and `POSTMORTEM.md`. Added from them: `DISCOVERY.md` (assumed numbers, labelled as such), `DECISIONS.md`, `labels.csv`, `usage.jsonl` (from the trace), `RESULTS.md`. Replayed offline, no model called: `retry_test.py` (hand-written malformed-then-good fixture in `replay/`, saved as `RETRY_TEST.txt`), `guard_test.py` (the model's saved reply for cfp-16, saved as `GUARD_TEST.md`; `adversarial/` holds a copy of that real posting), and `python3 extract.py --replay trace/session-p1.jsonl --force`, which reproduces every file in `outputs/` byte for byte. The live version of the agent is `extract_v0_live_2026-10-10.py`.

Domain: conference calls for papers. The 24 postings in `postings/` are invented (modelled on how real ones read); the people and events in them do not exist.

Read in this order:

0. `DISCOVERY.md`, `DECISIONS.md`, `COURSE_PROGRESS.md` (Model choice: b): the three sourced numbers, the choices, the model option.
1. `ONE_PAGER.md` : six headings, including the thing that must never happen.
2. `PREDICTION.md` : written before the labels and before any code.
3. `labels/LABELLING_RULES.md`, `labels/sample.json` : 15 postings labelled by hand before the agent ran.
4. `schema.json`, `validate.py`, `extract.py` : the agent. Standard library only.
5. `outputs/` : one JSON file per posting.
6. `eval.py`, `eval-v0.txt` : the score, per field, with the confident-wrong count kept separate.
7. `trace/` : the real run trace (`session-p1.jsonl`: each prompt, reply, stop reason, token count; `events.jsonl`: one line per posting). Model name replaced with `<model-id>`.
8. `run1.txt`, `run2.txt`, `run-twice-diff.txt` : the run and the run-twice check.
9. `RESULTS.md`, `RETRY_TEST.txt`, `GUARD_TEST.md`: the contract's result files.
10. `POSTMORTEM.md` : prediction versus measurement. Read this last, and read the section on the guard twice.

Run: `export LLM_API_KEY=... LLM_BASE_URL=... LLM_MODEL=...; python3 extract.py; python3 eval.py`
