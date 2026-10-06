# Warm-up mission — the job-watch agent

Free tier. One evening. Not portfolio; this one is for you.

## The situation

You want to know, without checking manually, when a job worth your
attention appears on a live job board. Deployed (deployed.so) lists
tens of thousands of live remote postings and publishes an MCP server
at `https://deployed.so/mcp` that any agent can call: search jobs,
filter by what matters, read a posting's details.

Your mission: build an agent in Claude Code (or Codex) that watches
that board for a search you care about and tells you what changed
since it last looked.

## Before you build: the two-line prediction

Write these two lines in a file called `PREDICTION.md` before anything
else. This habit is the course.

1. How many postings do you expect your search to return today?
2. What do you expect one full check to cost, in tokens?

Wrong numbers cost nothing. Unwritten numbers teach nothing.

## The mission

1. Connect your session to the board's MCP server and list the tools
   it offers. Read the tool descriptions the way your agent will.
2. Define your watch: one search (a role family, a seniority, a
   location rule) that you would genuinely want alerts for.
3. Build the loop: fetch matching jobs → compare against what you saw
   last time (your agent will need to remember; a plain file is enough,
   see note 7-5) → report only what is new or gone.
4. Run it twice in a row. The second run should report "nothing new"
   and change nothing (note 6-4 explains why we care).
5. Compare reality against `PREDICTION.md`. Write one sentence about
   the gap.

## Done means

- A repo containing your agent, its `PREDICTION.md`, and a README
  stating what it watches and how to run it.
- A second run that changes nothing.
- The gap sentence.

## Field notes that pair with this mission

Before: 3-1 to 3-4 (what you're driving). During: 6-1 (what makes this
an agent), 8-1 (what the MCP tools are). After: 7-5 if your memory file
got messy, 6-2 before you ever point a loop at anything that bills.

## What's next

The program's graded missions run your work against our harness:
hidden inputs, reruns, budgets, verified numbers in your repo. The
warm-up badge for this mission is coming; program details at
deployed.so/courses.
