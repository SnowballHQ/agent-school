---
description: Reveal a worked example of a mission, after your own attempt (or an explicit skip)
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Takes one argument: a mission id (`week0`, `warmup`, `project1`, `week3`; aliases `warm-up`, `p1`, `p2`/`w3` are accepted). If none is given, ask which one. Exemplar folders live in `${CLAUDE_PLUGIN_ROOT}/exemplars/`: `week0` -> `week0/`, `warmup` -> `warmup/`, `project1` -> `project1/`, `week3` -> `project2/` (the Week 3 eval exemplar). If the id has no folder, say there is no exemplar for it yet and stop.

**Step 1: find out whether the learner has had their go.** Read the mission's row in `COURSE_PROGRESS.md` (row ids are the canonical names: week0, warmup, project1, week2 to week8). Stop at the first that settles it:

- The status is `attempted`, `defended` or `skipped` -> go to Step 2b.
- The learner says they want to skip this mission, or see the answer without doing it -> write `skipped` into that row's status (and mark the skipped column) first, then go to Step 2b. A skip is a legitimate choice and is not judged; just record it.
- Otherwise -> Step 2a.

Never require a GitHub issue or a submission; `/agent-school:submit` is optional and has nothing to do with this gate. If `COURSE_PROGRESS.md` does not exist, treat the status as not attempted and offer the `/agent-school:setup` steps.

**Step 2a: not attempted yet.** Do not open, quote, summarise or hint at anything inside the exemplar folder. Say what it is in plain words: a finished version of this mission built by someone else, with the real trace, a prediction written before the run, and a postmortem of what the prediction got wrong. Say this one line to the learner: "I hold this back until you have had your own go because seeing a finished answer first turns your own attempt into copying, and the point of this mission is the mistakes you make yourself." Then offer the paths: `/agent-school:mission` to start or resume, `/agent-school:check` or `/agent-school:defend` once they have an attempt (either records it), `/agent-school:notes <number>` for a concept they are stuck on, or, if they would rather skip this mission, say so and you will mark it skipped and reveal it.

**Step 2b: unlocked.** Say which mission is unlocked. Read the folder's `README.md` and walk the learner through it in the order it gives, the trace and the postmortem first, the code last. Then ask them to compare: where did their prediction and the exemplar's prediction miss in the same direction, and what did the exemplar's postmortem find that theirs did not? (If they skipped, ask what they would have predicted, and what surprises them.) Do not tell them their work is worse; the exemplar is one run, not the answer. Do not paste the whole folder; open one file at a time and ask what they notice before explaining.

Exemplars never contain anything secret. They may contain real data (job titles, company names) copied as it appeared on the day.
