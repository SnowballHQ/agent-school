---
name: warm-up-mission
description: "The free warm-up mission: build a job-watch agent against the live Deployed MCP. Load when the user wants to start/continue the warm-up mission."
---

# Warm-up mission

Guide the user through the free warm-up mission. The brief is `./missions/warm-up.md`: read it in full before saying anything, and follow it faithfully. Do not change its steps, its definition of done or its order.

Rules:

1. **Prediction first.** The user must write `PREDICTION.md` (the two-line prediction in the brief) before any build step. If it does not exist, help them write it, but the numbers are theirs. Do not proceed until the file exists. Wrong numbers are fine; unwritten numbers are not.
2. **The MCP endpoint is configured by this plugin** (`deployed-jobs`, https://deployed.so/mcp). Use it for the live job board the mission watches. If its tools are not available, tell the user to check `/mcp` and restart the session.
3. **Let the user build.** Explain, ask questions and point at the matching field notes (3-1 to 3-4 before, 6-1 and 8-1 during), but the agent in their repo is theirs to write.
4. **Check against the brief's "Done means"**: the repo with agent, `PREDICTION.md` and README; a second run that changes nothing; the one-sentence gap between prediction and reality.
5. **When it is done**, point them to `/agent-school:enroll` for the full program.
