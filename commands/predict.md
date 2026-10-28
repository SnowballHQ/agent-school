---
description: Scaffold a PREDICTION.md before you build
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Create `PREDICTION.md` in the current directory if it does not exist (if it does, show it and ask whether to extend it). The filename is always exactly `PREDICTION.md`.

First, find the current mission: ask, or read `COURSE_PROGRESS.md` for the row marked `in-progress`. If it is known, read its brief under `${CLAUDE_PLUGIN_ROOT}/missions/` (the mission-to-file table is in `/agent-school:mission`) and copy that brief's own prediction questions into lines 1 to 3 below, replacing the generic ones. If the mission is not known, use the generic lines as written.

Write the structure below with the numbered questions but leave every answer blank for the learner; do not fill in numbers for them. Ask the questions one at a time and write down their answers.

```markdown
# Prediction

Written before building. Wrong numbers cost nothing; unwritten numbers teach nothing.

1. How many results do you expect today? (the count or output size you expect)
2. What do you expect one full run to cost, in tokens?
3. Expected accuracy: what fraction of outputs do you expect to be right, and how will you check?
4. Expected cost: per run and per month at the volume you intend.
5. Expected failures: which inputs or situations do you think will break it, and how?
6. Stability: if you run it twice on the same input, what do you expect to change?

## The gap

- Reality vs prediction, one sentence per line above:
```

Lines 1 to 3 are the brief's own prediction questions for the mission (copied from the brief when the mission is known); lines 4 to 6 extend them for bigger projects. Remind the learner that the file must exist before any build step, and that `/agent-school:gap` fills in the `## The gap` section after the run.
