# Requirement one-pager: conference call-for-papers tracker

**Honesty note.** I could not interview a real speaker for this exemplar, and I am an agent working with made-up postings. The quote below is a stand-in I wrote. Your discovery should rest on your own knowledge or public sources (see `DISCOVERY.md`), not an invented person. The 24 postings in `postings/` are invented but modelled on how real calls for papers read.

## The problem

> "I find calls for papers in newsletters and chat groups. By the time I open one, I've forgotten whether it closes next week or next year, and whether they'll pay for my flight. Twice I've found out a deadline had passed the week before." (stand-in quote)

Stakeholder: a developer who gives about six talks a year and wants a short, trustworthy list of open calls to choose from.

## The manual process today

She copies each call into a spreadsheet by hand: name, deadline, dates, place, whether travel is paid. About six minutes per posting.

Volume (assumed, to be replaced with her real counts): 40 new calls a month, so about 4 hours a month. The time is not the problem. The cost is the two or three calls a year she misses, each a talk she wanted to give.

Worth automating? Yes, narrowly: the saving is small, but extraction is the part that is dull and error-prone for a human, and a checked date is worth more than a fast one. If she only ever tracked five calls a month, the answer would be no.

## Inputs and outputs

In: the text of one call for papers. Out: one JSON object per posting with eight fields (seven are scored; `deadline_quote` is checked by code instead): `is_cfp`, `conference_name`, `submission_deadline` (a date, or null), `deadline_quote` (the exact words the date came from, or null), `event_start_date`, `format` (in_person, virtual, hybrid, unclear), `audience_level` (beginner, intermediate, advanced, all, unclear), `travel_support` (full, partial, none, unclear). The full definition is `schema.json`.

## What correct means

Run `python3 eval.py` against `labels/sample.json` (15 postings I labelled by hand before running the agent). It passes when both hold:

- At least 90% of the 15 x 7 = 105 labelled cells match the label exactly.
- The **confident-wrong deadline count is 0**: no posting where the agent gives a deadline date and the label says the date is something else, or that there is none.

## What must never happen

**A deadline reported as a specific date that the posting does not actually give.** Example: a posting says "abstracts are due six weeks before the event". An agent that works out a date, or picks "30 October" from a post that mentions two dates, hands the speaker a wrong date with full confidence. She plans around it, misses the true one, or travels for a call that closed.

What this line changed in the design (the mission asks for at least one, logged in `DECISIONS.md`, tested in `GUARD_TEST.md`):

1. The agent may return `null` for the deadline. A null costs her one minute of looking. A wrong date costs a talk. The prompt says so, and the schema allows it.
2. Every date must come with `deadline_quote`, the exact words it was read from. Code, not the model, checks that quote really appears in the posting. If it does not, the date is thrown away and replaced with null.
3. Accuracy is scored with the confident-wrong deadline count kept separate, so a high average cannot hide it.

## The budget

Time: one evening to build, under an hour to label. Money: under 0.50 USD for the 24-posting run, under 3 USD a month at 40 postings a month with room to retry. Latency does not matter; a batch can run overnight. Cost ceiling is enforced in the script (`max_completion_tokens` per call, two calls at most per posting).
