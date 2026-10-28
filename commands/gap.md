---
description: Draft the prediction-vs-reality gap sentence from your trace
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Fill in the "## The gap" section of `PREDICTION.md` from real numbers.

1. Read `PREDICTION.md` (stop and point to `/agent-school:predict` if it does not exist) and the learner's predictions, especially the token-cost line.
2. Read every `.course/trace/session-*.jsonl` (one JSON object per line: `role`, `text`, `model`, `usage`). If `.course/trace/` is missing or empty, say that setup was probably not run in this folder (the plugin only records inside a folder that has a `.course/` directory) and offer to run the `/agent-school:setup` steps now; recording starts from then on, so this run's trace cannot be recovered. Meanwhile ask the learner for the actual numbers instead. Numbers pasted from `claude -p --output-format json` output are accepted too: read the `usage` object (`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`) and `total_cost_usd`.
3. Total the usage tokens: sum `input_tokens`, `output_tokens`, `cache_creation_input_tokens` and `cache_read_input_tokens` across lines where `usage` is not null, and report each total plus a combined figure (and `total_cost_usd` when it was supplied). Say which sessions and how many messages you counted. Transcripts can contain the same message from resumed sessions, so mention it if numbers look doubled. Optionally count tool calls from `.course/trace/events.jsonl`.
4. Draft the gap: ONE honest sentence comparing predicted and actual (name both numbers and the ratio), plus ONE observation about why they differ, grounded in something visible in the trace (for example a retry loop, a large pasted file, or a prompt that was too vague). Quote the learner's own words if it helps. No flattery, no excuses.
5. Show the draft and let the learner edit it. Then write it into `PREDICTION.md` under a `## The gap` heading (add the heading at the end if missing; replace the body if it exists). The learner's words win over yours.
