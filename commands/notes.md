---
description: Browse all 43 field notes and read one (by number or topic)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Use the `field-notes` skill. The notes are a flat list of 43 (the start-here guide plus 42), free to read in any order.

- If the learner gave a number like `3-2`, open that note.
- If they gave a topic ("tokens", "idempotent", "evals"), pick the matching note from the skill's table and confirm it in one line before opening.
- If they gave nothing, ask what they are working on or which mission they are on (check `COURSE_PROGRESS.md` if it exists) and show the notes for that stage, or the cluster list if they ask for everything. Let them choose.

Then read the note file with the Read tool, teach from it as the skill describes, and offer its two-minute experiment.
