# Decisions

### D1: Key postings by slug, never by position
Decision: the memory is a map from `slug` to the posting's details, and every comparison is by key.
Alternatives: compare the list in order; key by title and company.
Why: the board sorts newest first, so a position-based comparison reports every posting as changed the moment one new posting arrives at the top. Titles repeat (two "AI Engineer" postings at one company here), slugs do not.
Evidence that would change it: the board reusing a slug for a different job, which would show as a `returned` with a different title.

### D2: Code does the diff; the model only writes the summary
Decision: new, gone and returned are decided by set comparison in `watch.py`. The model is called only with `--summarise`, on new postings, and never when nothing changed.
Alternatives: give the model the old and new lists and ask what changed.
Why: set comparison is free, exact and repeatable. When the first summary came back blank (attempt 1), the memory was still correct because the model was not part of it. The second run costs 0 tokens.
Evidence that would change it: a change that only judgement can see, such as "same role reposted with a new slug", would need a model step.

### D3: Write the memory file only when something changed
Decision: sorted keys, fixed indent, written through a temp file, and not written at all on a `nothing new` run.
Alternatives: always rewrite with a fresh `last_seen`.
Why: a run that finds nothing then leaves the file byte-identical, so the run-twice check is a plain hash comparison. The cost is that `last_seen` only moves on runs that change something.
Evidence that would change it: needing to know when a posting was last confirmed live, which would call for a separate heartbeat file.

### D4: Refuse a watch too wide to read fully
Decision: if the search needs more than `max_pages` (4 pages of 50), stop with an error before touching memory.
Alternatives: read the first pages and carry on.
Why: reading only part of the list makes older postings fall off the edge and look `gone`. A wrong `gone` is worse than no answer. The must-never line (a half-read list marking postings gone) is why this guard exists.
Evidence that would change it: the board's reply carries a `total`; if it were checked against what was collected, a wide watch could be allowed when the counts match.

### D5: No date window in the watch
Decision: the watch has no "posted in the last 30 days" filter.
Alternatives: a recency filter to keep the list short.
Why: a moving window pushes postings out of the results as they age and reports them `gone` when they are only old.
Evidence that would change it: a stable count of live postings that the board itself marks closed, so `gone` could mean closed rather than old.

### D6: Check why the model stopped before trusting its text
Decision: the summary step reads the reply's stop reason and prints `[summary unavailable ...]` out loud if it was not `stop`; the output allowance went from 2,000 to 6,000 tokens.
Alternatives: print whatever text came back.
Why: attempt 1 spent all 2,000 output tokens on hidden thinking and wrote nothing; the alert looked complete with a blank where the verdicts belonged. Only the stop reason in the trace showed it.
Evidence that would change it: a provider that reports thinking separately and never truncates the visible answer.
