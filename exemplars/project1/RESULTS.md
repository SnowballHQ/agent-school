# Results (v0 run of 2026-10-10; the fuller story is in POSTMORTEM.md)

Accuracy on reviewed sample: 11 of 15
Cell accuracy: 93 of 105 (88.6%), below my own 90% bar; confident-wrong deadlines: 2 (cfp-06, cfp-16)
Tokens in: 9151
Tokens out: 3429
Cost: not priced in dollars (the provider's per-token price was not recorded); 12,580 tokens for 24 postings, 524 per posting, from `usage.jsonl`. Hidden reasoning tokens, if any, are inside these counts.

The 15 reviewed rows are in `labels.csv`; 11 rows were fully right and the 4 with any wrong cell are cfp-02, cfp-06, cfp-16 and cfp-23. Nine postings were extracted but not labelled. Schema failures: 0, retries: 0 (the retry path is tested separately in `RETRY_TEST.txt`).

## The gap
1. Predicted 85% of cells; measured 88.6%. Within 4 points, but it fails my own bar because of the two confident-wrong deadlines.
2. Predicted about 850 tokens a posting and about 85,000 for one hundred; measured 524 a posting, about 52,000 for one hundred. I over-guessed the instruction length by about 60%.
3. Predicted travel_support fails most; it did, 11 of 15 (73%), because the schema has no value for "only for some people".
Unnumbered: I predicted 1 confident-wrong deadline and got 2, and my guard caught neither (`GUARD_TEST.md`).
