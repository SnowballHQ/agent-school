# Decisions

### D1: Multi-value audience level takes the lower one
Decision: for a posting that says "intermediate and advanced" the field `audience_level` holds one value, the lower bound (`intermediate`); "all levels" or "beginners and experts" is `all`. This multi-value rule is written in `labels/LABELLING_RULES.md` before the agent existed.
Alternatives: a list of levels; a range with two fields.
Why: one enum value per field keeps the schema flat and the scoring a plain equality check. The cost is that a posting aimed at two levels loses information.
Evidence that would change it: several postings where the lower bound sends the speaker to the wrong event. Note the v0 prompt did not include this rule, so some misses (cfp-06) come from my spec not being passed on.

### D2: Two deadlines or a relative deadline become null (multi-value dates)
Decision: if a posting gives two deadlines with no clear final one, only a relative one ("six weeks before the event"), or a date that could be day-first or month-first, `submission_deadline` is null. If a deadline is extended, the new date is the deadline.
Alternatives: pick the earliest; pick the latest; return a list of candidates.
Why: a null costs her one minute of looking; a wrong date costs a talk. This is the multi-value case that failed in the run: cfp-16 has a full-paper and an extended-abstract deadline and the model chose January.
Evidence that would change it: if most postings with two dates have an obvious main one, a list of candidates with code choosing null only on a tie would lose less.

### D3: The must-never line shaped the schema and the guard (must-never)
Decision: must-never is "a deadline reported as a specific date that the posting does not give". So: the deadline may be null, every date comes with `deadline_quote`, and code (not the model) drops the date if the quote is not in the posting.
Alternatives: trust the model's date; ask the model to grade its own date.
Why: the expensive mistake is a confident wrong date, so the design makes the safe answer cheap (null) and the dangerous answer need evidence.
Evidence that would change it: the guard missed both confident-wrong deadlines (`GUARD_TEST.md`) because it checks that the quote exists, not that the date follows from it. Next version: code checks that the date, in the posting's own format, appears inside the quote.

### D4: Score confident-wrong deadlines separately from accuracy
Decision: `eval.py` reports cell accuracy and the confident-wrong deadline count as separate lines, and passes only with at least 90% and zero confident-wrong.
Alternatives: one average over all cells.
Why: an average can hide the one failure that matters; here 88.6% looks nearly fine while 2 confident-wrong deadlines are the real result.
Evidence that would change it: a labelled sample large enough that a single posting stops moving the percentage by 6.7 points.

### D5: Label first, from my own head, before any agent code
Decision: 15 postings were hand-labelled with written rules before `extract.py` was written; the agent's outputs were never looked at while labelling (`labels.csv`, `labels/sample.json`).
Alternatives: label after seeing the outputs; label a bigger sample.
Why: labels made after seeing answers drift toward the answers. The cost is that one head wrote the postings, labels and prompt.
Evidence that would change it: a second labeller disagreeing on cfp-02, cfp-06 or cfp-23, which were close calls; fix the label rule before the agent.

### D6: Retry once, then record a failure, never pass it on
Decision: an answer that fails `schema.json` is retried once with the problems listed; a second failure goes to `failures.jsonl` as `{id, reason}` and no output file is written.
Alternatives: accept the first answer; retry until valid.
Why: a retry loop with no limit is how a bill grows; a silent pass-through is how bad data enters the list. The real run had 0 schema failures, so this path was only exercised by the offline test in `RETRY_TEST.txt`.
Evidence that would change it: more than a few percent of postings needing the retry would mean fixing the prompt rather than retrying.
