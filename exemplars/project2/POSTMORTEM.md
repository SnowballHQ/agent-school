# Postmortem

## Prediction vs measured

| | Predicted | Measured (submitted run) |
|---|---|---|
| remote_type accuracy | 0.80 | 0.85 |
| seniority accuracy | 0.55 | 0.95 |
| cost, one pass | about $0.02 | about $0.018 (at an assumed price) |
| second run identical | yes | no on fresh caches (1 of 20 lines); yes with a cache |

## The surprise: seniority

I expected seniority to be the weak field because the label habits looked arbitrary (director-level roles as exec, a freelance trainer as junior). It was the strong one, 0.95. A short rubric that says "read the title first, then the years asked for" was enough for the model. Remote type, which I thought was easy, was where the misses were: three of the four errors. I did not re-read each of those postings closely enough to say whether the label or the model is wrong; that is the first thing to check, and it is the reading you should do before touching the prompt. The one seniority miss, "Associate Director" read as lead rather than exec, is a rubric gap, not a model failure.

The second surprise was determinism. Setting temperature to zero did not make two fresh runs match; the model has hidden reasoning and the borderline posting (a plain "Software Engineer", mid or junior) flipped. Majority voting cut the differences from 2 to 1, not to 0.

## What a student should try differently

- Do not trust temperature 0. Test run-twice with an empty cache early, and look at which postings flip: those are the ones the rubric does not decide.
- Fix flip-prone postings with a rule, not another vote. A line like "no seniority word and no years stated means mid" removes the coin toss.
- Read your misses and ask whether the label or the model is wrong. Here the Associate Director case needs a sentence in the rubric.
- Do not spend three calls per posting for accuracy: attempt 1 scored the same as the vote on the first pass. Votes buy stability, and not enough of it.
- On the hidden set, classes with one or two examples make per-class recall jumpy; check your confusion table, not just accuracy.
