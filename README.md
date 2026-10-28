# Agent School

**Agent School** is a free, self-paced course in building and checking AI agents: eight weeks plus pre-work, run entirely inside Claude Code next to your own project. No account, no payment, no cohort. Start anywhere and skip what is too basic.

## Install

```
claude plugin marketplace add SnowballHQ/agent-school
claude plugin install agent-school@agent-school
```

Then, in an empty folder for your work, run `/agent-school:setup` and `/agent-school:mission`.

## The ten missions

Pick any, in any order: `week0` (first call, first trace), `warmup` (the job-watch agent), `project1`, and `week2` to `week8`. Each brief says what to build, what to predict before you build, and what done means.

## The 43 field notes

The start-here guide plus 42 short notes in eleven clusters, from what a model is doing to how to present a failure. Each ends with a two-minute experiment. Ask for one by number (`3-2`) or topic with `/agent-school:notes`.

## Commands

- `/agent-school:setup`: set up the folder (`.course/` trace marker, `COURSE_PROGRESS.md`).
- `/agent-school:mission`: pick a mission and start or resume it.
- `/agent-school:notes`: browse the notes and read one.
- `/agent-school:predict`: write `PREDICTION.md` before you build.
- `/agent-school:gap`: fill the `## The gap` section from your real token numbers.
- `/agent-school:check`: run the mission's local checks.
- `/agent-school:defend`: the oral defense; feedback on your thinking is written into `COURSE_PROGRESS.md`.
- `/agent-school:exemplar`: reveal a worked example after your own attempt (or an explicit skip).
- `/agent-school:submit`: optional; open a public portfolio issue on SnowballHQ/agent-school-submissions.
- `/agent-school:progress`: see where you are and what to try next.
- `/agent-school:next`: what comes after: Course 2 and the Deployed board.

Skills: `mentor` (hints in a fixed order, prediction discipline) and `field-notes`. `.mcp.json` connects the live Deployed job board (https://deployed.so/mcp).

## Choosing a model

The agents you build run on a model you choose, and choosing is part of the learning. Most people use Claude Code's print mode on their existing subscription (`claude -p --output-format json` returns the answer plus `usage` and `total_cost_usd`, no API key needed). The alternatives are an API key from a model provider, or another provider altogether. Week 0 walks through the trade-offs and asks you to record your choice in `COURSE_PROGRESS.md`; start there if you are unsure.

## What the plugin records

This plugin keeps a local record of your work so the mentor and reviewers can give feedback on what actually happened, not on a summary of it. It follows the same rule as note 9-1: send only what the task needs, and say plainly what leaves your machine.

- **What.** For each tool call: the tool name and a short summary (file path, or the shell command; strings capped at 500 characters). For each conversation: the full text of your prompts and the replies, with the model and token counts.
- **Where.** In your own project repo, under `.course/trace/`. Nothing is sent anywhere by the plugin.
- **When it records.** Only in a repo that has a `.course/` directory (the course repo marker). Anywhere else the hook does nothing.
- **When it travels.** Only when you run `/agent-school:submit`. The traces ride along inside your repo, so you commit them first, and the command asks before staging `.course/trace/`. If you never submit, they never leave your machine.
- **The scrub.** Before anything is written, API keys (`sk-ant-...`, `sk-...`, AWS `AKIA...`), bearer tokens and lines like `api_key=...`, `token: ...`, `password=...` or `secret=...` have their values replaced by `[REDACTED]`. A scrub is a safety net, not a guarantee: do not paste secrets or other people's personal data into prompts in the first place.
- **How to delete.** `rm -rf .course/trace` removes everything the plugin recorded. You can read it first: it is plain JSON lines.

Consent is yours slice by slice: recording locally is on in course repos, sharing is a separate act you choose by submitting.
