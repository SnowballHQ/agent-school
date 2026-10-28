# Decisions

### D1: Which model option to run on
Decision: option (b), an API key held in an environment variable, with the address and model name also in variables so the script is not tied to one provider.
Alternatives: (a) Claude Code print mode on a subscription; (c) another provider's own script.
Why: this exemplar was built by an agent working on an API key, and a plain HTTP call shows every field of the request and reply, which is what the trace-reading step needs. The whole mission cost well under a cent.
Evidence that would change it: a learner with no key and no card would switch to (a); a bill above a few dollars for the course would make me ration calls.

### D2: Cap the reply at 400 tokens
Decision: send `max_completion_tokens: 400` on every call.
Alternatives: no cap; a cap of 50.
Why: output is the part of the bill I do not control, so I set the ceiling myself. 400 is far above the 28 to 36 tokens a one-sentence answer takes, so it never cuts a reply; a cap of 50 would have sat too close to the real output.
Evidence that would change it: any run with `finish_reason` of `length` means the cap cut an answer and needs raising.

### D3: Redact the key in the trace
Decision: write `Bearer [REDACTED]` into `raw-calls.jsonl` and replace the provider address and model name with placeholders before sharing.
Alternatives: save the exact request headers; save no raw trace.
Why: a trace I cannot safely share is a trace I will stop saving. The must-never line (key written into a file) is the reason the header is rewritten before it is saved, not after.
Evidence that would change it: if a provider put secrets in the reply body, I would redact the reply too.

### D4: Keep three same-question runs and one changed question
Decision: three runs of question A and one of question B, as the mission asks.
Alternatives: ten runs of A for a firmer picture of variation.
Why: three is enough to see that replies and output counts differ; one changed question shows that input count follows the question and not the run.
Evidence that would change it: if I needed a variation range (for example to set an alert threshold) I would take ten or more.
