# Decisions

### D1: Which model
Decision: Claude Code print mode.
Alternatives: API key; another provider.
Why: no key on a subscription.
Evidence that would change it: usage limits hit.

### D2: multi-value seniority
Decision: store the lower bound.
Alternatives: list; range.
Why: simplest to compare.
Evidence that would change it: many ranged postings.

### D3: must-never guard
Decision: guard compares dates, not only quotes.
Alternatives: quote-exists only.
Why: a real quote can back a wrong date.
Evidence that would change it: guard blocks good rows.
