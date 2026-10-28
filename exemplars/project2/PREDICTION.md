# Prediction (written before the first real run)

Dev set: 20 postings, one model call each.

| Field | Predicted accuracy | Reasoning |
|---|---|---|
| remote_type | 0.80 | Most postings say remote, hybrid or an office city outright; the misses will be postings that are silent, where the label may not match my "silent means onsite" rule. |
| seniority | 0.55 | Titles carry the signal, but the labels have their own habits (what counts as lead vs staff vs exec, where freelance or analyst roles land) that a rubric written from the title alone will not guess. |

Predicted cost: about $0.02 for one pass over the 20 postings (about 20 calls, roughly 1,000 input and 30 output tokens each), because the postings are short and the answer is a tiny JSON object. The price per token is my assumption, since the meter's table is not visible to me.

Predicted idempotency: identical on the second run, helped by temperature 0 and an on-disk cache.
