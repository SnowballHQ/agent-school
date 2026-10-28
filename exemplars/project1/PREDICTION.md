# Prediction (written after the one-pager and the postings, before any label was made and before any agent code)

## Predictions

1. **What accuracy will v0 reach on my reviewed sample?**
   Cell-level (105 cells): **85%**. I expect most fields to be easy and two or three postings that are built to be tricky to cost me a handful of cells each. This is below the 90% target in my own test, so I expect the first run to fail it.

2. **What will one posting cost, in tokens, and what will one hundred cost?**
   The posting is about 200 tokens, the instructions and schema about 500, and the JSON answer about 120. Roughly **850 per posting**, so about **85,000 for one hundred**, assuming no retries. If the model spends hidden thinking tokens the way I think it might, double that.

3. **Which field will fail most often, and why?**
   **travel_support.** The postings describe it in many different ways ("case by case", "up to a cap we will confirm", "local speakers only"), and the line between `partial` and `unclear` is a judgment call even for me.

- **Also predicted (not numbered): how many confident-wrong deadlines?** I predict **1**: the posting with two dates or the one with the day-and-month written as numbers will trip it.

- **Also predicted (not numbered): how many outputs will fail the schema on the first try?** **0 or 1** of 24, and the retry will fix it.

## The gap
1. Accuracy: I said 85% of the 105 labelled cells; v0 got 88.6% (93 of 105), which is 11 of the 15 rows fully right. Close, but it still fails my own bar of 90% with zero confident-wrong deadlines.
2. Cost: I said about 850 tokens per posting and 85,000 for one hundred; the run used 524 per posting (12,580 for 24: 9,151 in, 3,429 out), so about 52,000 for one hundred. I over-guessed the instructions.
3. Worst field: travel_support, as predicted, 11 of 15 (73%), because "only some people qualify" has no value in the schema.
Unnumbered: confident-wrong deadlines were 2, not 1 (cfp-06 and cfp-16); no output failed the schema, so the retry path never ran in the real run (`RETRY_TEST.txt` tests it separately). Full account: `POSTMORTEM.md` and `RESULTS.md`.
