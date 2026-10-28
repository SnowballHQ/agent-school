# Guard test

posting: adversarial/cfp-16-two-deadlines.txt
result: missed

What this is. The posting is a copy of cfp-16 from the real run (`postings/cfp-16.txt`), kept as the adversarial case because it beat the guard in `extract.py`: it gives two deadlines (full paper 20 November 2026, extended abstract 15 January 2027) and a real quote supports the wrong choice. It was found by scoring the real run, not designed in advance; the cfp-06 case ("six weeks before the event") failed the same way.

What happened. The model answered 2027-01-15 with the quote "Extended abstract deadline: 15 January 2027." That quote does appear in the posting, so the guard (which only checks that the quote exists) kept the date. The hand label for the deadline is null, so the guard missed a confident wrong answer. Reproduce offline with `python3 guard_test.py` (it reads the model's saved reply from `trace/session-p1.jsonl`; no model is called).

What would work: have code check that a date, written in the posting's own format, appears inside the quote, and return null when the posting shows more than one candidate deadline. See `POSTMORTEM.md`.
