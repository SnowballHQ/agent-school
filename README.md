# Agent School (free starter)

**Agent School** — Deployed's agent engineering program.

This plugin is the free starter for the program: nine foundations field notes and the warm-up mission, packaged for Claude Code so the notes can be read, explained and quizzed inside your own project.

## Install

```
claude plugin marketplace add SnowballHQ/agent-school
claude plugin install agent-school@agent-school
```

## What is inside

- `notes/`: nine short notes on what a model does, tokens, context windows, why answers differ between runs, what an agent is, and what an API is. Each ends with a two-minute experiment.
- `missions/1-warmup.md`: the warm-up mission. You build a small agent that watches a live job board and reports what is new, and you write down predictions before you build.
- `skills/field-notes`: lets Claude open and teach from the notes, and re-explain them with your project as the example.
- `skills/warm-up-mission`: walks you through the mission and holds you to the prediction step.
- `.mcp.json`: connects the live Deployed job board (https://deployed.so/mcp), which the warm-up mission uses.

## Commands

- `/agent-school:notes`: list the notes and pick one.
- `/agent-school:mission`: start or resume the warm-up mission.
- `/agent-school:enroll`: what the full program is and how to join.

## The full program

Ten weeks, four graded projects and a capstone, checked by a harness. Details and the waitlist: https://deployed.so/courses
