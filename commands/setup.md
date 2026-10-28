---
description: Set up this folder for Agent School (trace marker, progress file)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Set up the current folder for Agent School. Safe to run any number of times; never overwrite or truncate anything that already exists.

1. Create `.course/` and `.course/trace/` if missing (`mkdir -p .course/trace`). `.course/` is the marker: the plugin's trace hook records only in a folder that has it.
2. If `COURSE_PROGRESS.md` does not exist, create it from the template below (ask the learner for an optional name first; blank is fine) and put today's date under Started. If it exists, leave it untouched and say so.
3. Tell the learner, in four lines:
   - The plugin records tool calls and your conversation text (prompts, replies, model, token counts) into `.course/trace/`, in this folder only.
   - Secrets such as API keys and bearer tokens are scrubbed before anything is written; that is a safety net, not a guarantee.
   - Nothing leaves your machine unless you run `/agent-school:submit`. The traces are plain JSON lines you can read, commit (they are committable like any file) or delete with `rm -rf .course/trace`.
   - `COURSE_PROGRESS.md` is yours: `/agent-school:check`, `/agent-school:defend` and `/agent-school:exemplar` update it, and you can edit it by hand.
4. End by pointing at `/agent-school:mission` to pick a starting point (any mission, in any order).

Template for `COURSE_PROGRESS.md`:

```markdown
# Course progress

## Learner

Name (optional):

## Started

<YYYY-MM-DD>

## Model choice

(blank until Week 0: which model your built agents run on, and why)

## Missions

Status is one of: not-started, in-progress, attempted, defended, skipped.

| mission | status | checked | defended | skipped | notes |
|---|---|---|---|---|---|
| week0 | not-started | | | | |
| warmup | not-started | | | | |
| project1 | not-started | | | | |
| week2 | not-started | | | | |
| week3 | not-started | | | | |
| week4 | not-started | | | | |
| week5 | not-started | | | | |
| week6 | not-started | | | | |
| week7 | not-started | | | | |
| week8 | not-started | | | | |
```
