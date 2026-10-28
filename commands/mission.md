---
description: Pick a mission and start or resume it (any order, skip freely)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Missions (a flat menu; there is no required order and no gate):

| id | mission | brief |
|---|---|---|
| week0 | Week 0: first call, first trace | `${CLAUDE_PLUGIN_ROOT}/missions/0-week0.md` |
| warmup | Warm-up: the job-watch agent | `${CLAUDE_PLUGIN_ROOT}/missions/1-warmup.md` |
| project1 | Project 1 | `${CLAUDE_PLUGIN_ROOT}/missions/2-project1.md` |
| week2 | Week 2 | `${CLAUDE_PLUGIN_ROOT}/missions/3-week2.md` |
| week3 | Week 3 | `${CLAUDE_PLUGIN_ROOT}/missions/4-week3.md` |
| week4 | Week 4 | `${CLAUDE_PLUGIN_ROOT}/missions/5-week4.md` |
| week5 | Week 5 | `${CLAUDE_PLUGIN_ROOT}/missions/6-week5.md` |
| week6 | Week 6 | `${CLAUDE_PLUGIN_ROOT}/missions/7-week6.md` |
| week7 | Week 7 | `${CLAUDE_PLUGIN_ROOT}/missions/8-week7.md` |
| week8 | Week 8 | `${CLAUDE_PLUGIN_ROOT}/missions/9-week8.md` |

Steps:

1. **Setup.** If `.course/` does not exist in the current folder, read `${CLAUDE_PLUGIN_ROOT}/commands/setup.md` with the Read tool and run its steps inline now, using its `COURSE_PROGRESS.md` template verbatim (the six-column table; `check` and `defend` write into those columns) before anything else. Do not just tell the learner to run it.
2. **Choose.** If the learner has not said which mission, show the menu with each mission's status from `COURSE_PROGRESS.md` and ask where they want to start. Anyone may start anywhere and skip what is too basic; never insist on Week 0 or on an earlier mission. If they say a mission is too basic, offer to mark it `skipped` in the progress file.
3. **Read the brief** with the Read tool, in full, and follow it faithfully. Do not change its steps, its definition of done or its order.
4. **Resume or start.** Look in the current folder for the files the brief names as its deliverables or intermediate artifacts (for example `PREDICTION.md`, a README, scripts, run logs, the eval files). Say whether the learner is starting or resuming, and continue from the right step of the brief.
5. **Progress.** Set the mission's row in `COURSE_PROGRESS.md` to `in-progress` (unless it already says attempted, defended or skipped; do not downgrade).
6. **Teach.** Apply the `mentor` skill throughout, and surface the notes for the current step through the `field-notes` skill (offer, do not dump).
7. When the learner thinks they are done, point at `/agent-school:check` (local checks) and `/agent-school:defend` (the oral defense), then `/agent-school:exemplar` and `/agent-school:next`.


Aliases accepted for the ids above: `warm-up` = warmup, `p1` = project1, `w2`…`w8` = week2…week8. Use the canonical id in `COURSE_PROGRESS.md`.
