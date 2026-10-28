---
description: Show your course progress and suggest what to try next
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

1. Read `COURSE_PROGRESS.md` in the current folder. If it does not exist, say the folder has not been set up and offer to run the `/agent-school:setup` steps now.
2. Show the learner name (if any), start date, model choice and the mission table in plain words: which missions are in progress, attempted, defended or skipped, and which are not started. Note anything stamped in the notes column (such as a submission issue link).
3. If `.course/trace/` exists, say how many trace files it holds.
4. Suggest ONE next mission: the first not-started or in-progress mission after the learner's most recent activity, with a sentence on why. This is only a suggestion; the learner may start anywhere. Never block or lecture about order.
5. Point at `/agent-school:mission` to start it.
