---
description: Oral defense of your thinking for a mission, or record a skip (e.g. /agent-school:defend p1)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Takes one argument: a canonical mission id (`week0`, `warmup`, `project1`, `week2` ... `week8`), optionally followed by `skip`; aliases `warm-up`, `p1`, `w2` ... `w8` are accepted (normalise to canonical for rubric filenames and `COURSE_PROGRESS.md`). If none is given, read `COURSE_PROGRESS.md` and ask which. Use the `examiner` skill at `${CLAUDE_PLUGIN_ROOT}/skills/examiner/SKILL.md` and the rubric `${CLAUDE_PLUGIN_ROOT}/skills/examiner/rubrics/<mission>.md`; follow them exactly. Mission briefs are in `${CLAUDE_PLUGIN_ROOT}/missions/`.

Summary: read the learner's files, ask the rubric's probes one at a time, write `FEEDBACK.md` and update `COURSE_PROGRESS.md`. Scores never block anything. If the learner says they want to skip, run the skip flow in the examiner skill instead.
