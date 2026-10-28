---
description: Run the deterministic local checks for a mission (e.g. /agent-school:check p1)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Takes one argument: a canonical mission id (`week0`, `warmup`, `project1`, `week2`, `week3`, `week4`, `week5`, `week6`, `week7`, `week8`); aliases `warm-up`, `p1`, `w2` ... `w8` are accepted and normalised by the script. Use the canonical name in `COURSE_PROGRESS.md`. If none is given, read `COURSE_PROGRESS.md` and ask which. Use the mentor skill's rules.

1. Run, from the learner's mission folder (ask which folder holds the mission if unclear; default is the current directory):

   `python3 "${CLAUDE_PLUGIN_ROOT}/checks/check.py" <mission> .`

   The script is read-only on the learner's files except that it runs the commands the mission's "Local check contract" names (run-twice, kill check, score.py) with a timeout. It prints one `PASS` or `FAIL <reason>` line per contract bullet and a final line `check <mission>: N/M passed`.
2. Show the output verbatim. Do not summarise it away and do not soften a FAIL.
3. Stamp the `checked` cell of the mission's row in `COURSE_PROGRESS.md` with the date and `N/M` (for example `2026-10-28 5/6`). Create the row if missing. Do not touch `status` unless every check passed and the learner asks.
4. For each FAIL, point at the matching field note or mission section (`${CLAUDE_PLUGIN_ROOT}/notes/`, `${CLAUDE_PLUGIN_ROOT}/missions/`) and ask the learner what the failure tells them about their brief. **Never fix the learner's files.** If a fix means rebuilding, send them back to the brief first (mentor rule 3).
5. A pass proves format and mechanics only. Say so, and offer `/agent-school:defend <mission>` for feedback on the thinking. Nothing here blocks progress.
