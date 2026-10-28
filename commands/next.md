---
description: What comes after this mission, or after the course
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Say plainly what to do next. Use only the facts below.

- **Next mission.** Read `COURSE_PROGRESS.md` if it exists and point at the next unattempted mission with `/agent-school:mission`, or `/agent-school:progress` for the whole picture. Any order is fine.
- **Course 2: RL environments and evals.** The follow-on course. It is free, self-paced, and its plugin (`course2`) installs from the same marketplace as this one. Install it with `claude plugin marketplace update agent-school`, then browse and install `course2` from `/plugin`.
- **The Deployed board.** The Deployed job-board MCP server (`deployed-jobs`, https://deployed.so/mcp) is already configured by this plugin. Use `/mcp` to confirm it is connected, then point your own agents at it: it is a live, real data source for something you build next.
- Optional: `/agent-school:submit` records a finished mission as a public issue, as a portfolio record.

Do not state prices, dates, durations, placement or job promises, or any statistic. For anything not listed here, say "check https://deployed.so/courses".
