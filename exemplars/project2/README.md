Unlocks after your P2 submission — reading it early cheats only yourself.

# Project 2 exemplar: job-posting extraction

A small pipeline that reads job postings and labels each one with two fields: `remote_type` (remote, hybrid, onsite) and `seniority` (intern, junior, mid, senior, lead, staff, exec). It is shaped exactly like a harness submission.

Files
- `harness.yaml`, `pipeline.py` — the submission itself (standard library only, so `install` is a no-op).
- `eval.py` — scores an output file against the dev labels, same per-field precision/recall/accuracy as the grader.
- `PREDICTION.md` — written before the first real run.
- `runs/` — both runs' outputs, the call trace, and `diff.txt` (run-twice check).
- `RESULTS.md`, `POSTMORTEM.md` — what was measured and what we learned.
- `FEEDBACK-P2.md` — places where the brief was ambiguous.

Run it locally

    export HARNESS_INPUT_DIR=../../../harness/datasets/p2/dev/inputs
    export HARNESS_OUTPUT=runs/run1.jsonl
    python3 pipeline.py
    python3 eval.py runs/run1.jsonl
