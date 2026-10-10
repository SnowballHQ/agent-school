---
title: "Warm-up: the job-watch agent"
access: free
---
# Warm-up: the job-watch agent

Free tier. One evening. Not portfolio; this one is for you.

## The three ideas you need

1. **An agent is a goal, some tools and a loop.** A **tool** is a function the model may ask your program to run, such as "search the job board." The **loop** is: look, decide, act, look again. A chatbot only talks. An agent acts, which is why its mistakes become actions. Field note: "What turns a chatbot into an agent?"
2. **Your agent talks to the board through an MCP server.** An **MCP server** is a program that publishes a list of tools in a standard way, so any agent can discover and call them. Deployed publishes one at `https://deployed.so/mcp`. The tool descriptions are what your agent reads to decide what to do, so read them the way it will. Field note: "What is an API, really?"
3. **Run it twice, and nothing may change.** Something that is **idempotent** leaves the world in the same state whether you run it once or twice. Your agent needs a memory of what it has already seen, and a plain file is enough. Without it, the second run reports everything again as new. This is the lesson of the whole mission. Field notes: "What happens when you run it twice?" and "Where does an agent keep its state?"

## The mission

Build an agent that watches the Deployed board for a search you care about and tells you only what changed since it last looked.

1. Connect your session to the board's MCP server and list its tools. Read each description.
2. Choose your watch: one search, such as a role family plus a seniority plus a location rule, that you would truly want alerts for.
3. Build the loop. Fetch matching jobs. Compare them to your memory file. Report only postings that are new or gone. Then update the memory file.
4. Give every posting a **key**, a value that stays the same across runs, such as the posting's id. Compare by key, never by position in a list.
5. Run it twice in a row. The second run must print "nothing new" and leave your memory file unchanged.

## Deliverable and how it's checked

A repo containing your agent, `PREDICTION.md`, and a README stating what you watch and how to run it.

The check is the **run-twice diff**. Snapshot your memory file, run again, snapshot again, and compare: the memory-file diff must be empty, and the second run must print "nothing new". The outputs of the two runs will differ by design, because the first lists postings and the second says nothing changed; it is the memory file that must not move. If a mentor or the harness finds even one repeated or reordered posting, the check fails and tells you which one. You also write one sentence on the gap between your predictions and what you saw.

## Predict before you build

Write these in `PREDICTION.md` first.

1. How many postings will your search return today?
2. What will one full check cost, in tokens?
3. If the board changes between your two runs, how many new postings do you expect to see?

## When you're stuck

- Run `/mission` and the mentor resumes you at the right step.
- Run `/notes 6-4` if the second run is not empty. Run `/notes 7-1` if your memory file got messy. Run `/notes 6-2` before you point any loop at something that bills.
- Permission slip for the cohort channel: "My second run is not empty, here is the diff." Pasting the diff is the fastest way to get help.
