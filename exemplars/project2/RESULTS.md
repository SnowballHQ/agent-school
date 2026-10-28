# Results (dev set, 20 postings)

Two attempts. The submitted pipeline is attempt 2 (three calls per posting, majority vote). Attempt 1 (one call per posting) is kept in `attempt1-single-call/`.

## Attempt 2 (submitted): `runs/run1.jsonl`, scored with `eval.py`

Coverage 1.00.

| Field | Precision | Recall | Accuracy | n |
|---|---|---|---|---|
| remote_type | 0.85 | 0.85 | 0.85 | 20 |
| seniority | 0.96 | 0.93 | 0.95 | 20 |

Misses (gold -> predicted): 12030 remote_type remote -> onsite; 22906 remote_type onsite -> hybrid; 22906 seniority exec -> lead; 27858 remote_type hybrid -> remote.

## Cost and tokens

- One pass, attempt 2 (60 calls): 56,715 input tokens, 1,727 output tokens (about 720 of the output were hidden reasoning tokens). The trace is `runs/trace.jsonl`.
- One pass, attempt 1 (20 calls): 18,905 input, 549 output.
- Dollar figure: the meter's price table is not visible to us, so this is an estimate at an assumed $0.25 per million input and $2 per million output tokens: about **$0.018 per pass for attempt 2**, about $0.006 for attempt 1. Total spend building this exemplar (four full passes plus a cached rerun that made no calls) is well under $0.10. Far inside the $2.00 budget either way.

## Run-twice check (`diff.txt`)

- Attempt 1, two runs with fresh caches: **not identical**, 2 of 20 postings differed (25138 seniority, 27858 remote_type). See `attempt1-single-call/diff.txt`.
- Attempt 2, two runs with fresh caches: **not identical**, 1 of 20 differed (25138 seniority, mid vs junior). Run 2 scored remote_type 0.85, seniority 0.90.
- Attempt 2, second run reusing the first run's cache: identical (exit 0), but only because it made zero model calls.

So determinism here depends on the cache. Whether the harness's two runs share `/tmp` is not documented (see FEEDBACK-P2.md item 4); if they do not, expect roughly one differing line out of 20.
