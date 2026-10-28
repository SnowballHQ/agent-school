---
name: field-notes
description: "All field notes of the Agent School, with the mission-order reading path. Load when the learner asks to read or learn a concept, hits a problem a note answers, or asks what to read next."
---

# Field notes

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

The start-here guide and all 42 notes live in `${CLAUDE_PLUGIN_ROOT}/notes/`, grouped here by cluster. The notes are free and can be read in any order. Note numbers are cluster-order (3-2 is cluster 3, note 2).

### Cluster 0: Start here

| # | Note | What it covers | File |
|---|---|---|---|
| 0-1 | How should I use these notes? | Forty-two short notes, two ways through them, and one trick that makes them yours. | ${CLAUDE_PLUGIN_ROOT}/notes/0-1-how-to-read-these-notes.md |

### Cluster 1: AI deployment mindset and FDE responsibilities

| # | Note | What it covers | File |
|---|---|---|---|
| 1-1 | What does a forward-deployed engineer actually do? | The job title sounds like software, and the code turns out to be the smallest slice of it. | ${CLAUDE_PLUGIN_ROOT}/notes/1-1-what-does-an-fde-do.md |
| 1-2 | Why does the demo always work and production always surprise you? | A demo runs on the data you chose. Production runs on all of it, and all of it includes the rows you never looked at. | ${CLAUDE_PLUGIN_ROOT}/notes/1-2-demo-vs-production.md |
| 1-3 | Who pays when the AI is wrong? | Mistakes are not equal in price. Find the one that costs the most and build the system around stopping that one. | ${CLAUDE_PLUGIN_ROOT}/notes/1-3-who-pays-when-ai-is-wrong.md |

### Cluster 2: Business problem discovery and requirement mapping

| # | Note | What it covers | File |
|---|---|---|---|
| 2-1 | How do you find the problem actually worth automating? | Three numbers decide whether a task deserves automation, and sometimes the right answer is to walk away. | ${CLAUDE_PLUGIN_ROOT}/notes/2-1-the-problem-worth-automating.md |
| 2-2 | What does a good requirement one-pager look like? | One page, six headings, and a single hard constraint that can reshape the whole system behind it. | ${CLAUDE_PLUGIN_ROOT}/notes/2-2-the-requirement-one-pager.md |
| 2-3 | Why do stakeholders say \"automate everything\" and mean \"don't touch anything\"? | People ask for full automation and then get nervous at the first sign of it. Trust arrives in slices. | ${CLAUDE_PLUGIN_ROOT}/notes/2-3-automate-everything-touch-nothing.md |

### Cluster 3: GenAI and LLM foundations

| # | Note | What it covers | File |
|---|---|---|---|
| 3-1 | What is a model actually doing when it answers you? | It has exactly one trick, repeated very fast. Once you see the trick, you'll understand both why it's so good and why it sometimes makes things up with a straight face. | ${CLAUDE_PLUGIN_ROOT}/notes/3-1-what-is-a-model-actually-doing.md |
| 3-2 | What are tokens, and why does anyone count them? | Every AI system has a meter running in both directions. Most people only discover this when the bill arrives. | ${CLAUDE_PLUGIN_ROOT}/notes/3-2-what-are-tokens.md |
| 3-3 | What is a context window, and what happens when it fills up? | A model can only consider what's in front of it right now, and the space in front of it has a hard edge. What falls past that edge simply doesn't exist for it. | ${CLAUDE_PLUGIN_ROOT}/notes/3-3-what-is-a-context-window.md |
| 3-4 | Why does the same question get different answers? | A system that gave the right answer once has told you almost nothing. Here is why, and what we do about it. | ${CLAUDE_PLUGIN_ROOT}/notes/3-4-why-different-answers-each-time.md |

### Cluster 4: Prompt engineering for business use cases

| # | Note | What it covers | File |
|---|---|---|---|
| 4-1 | Why do vague prompts produce confident garbage? | The model will always answer. When you leave gaps in the request, it fills them with the most average guess available, in a perfectly assured voice. | ${CLAUDE_PLUGIN_ROOT}/notes/4-1-vague-in-garbage-out.md |
| 4-2 | What is a structured output, and why do businesses insist on it? | A database can't store a paragraph. Getting a model to answer in fields instead of prose is where prompt work stops being writing and starts being design. | ${CLAUDE_PLUGIN_ROOT}/notes/4-2-structured-outputs.md |
| 4-3 | How do examples teach a model what you mean? | Some instructions can't be explained but can be shown. A handful of well-chosen examples often does more than a page of rules. | ${CLAUDE_PLUGIN_ROOT}/notes/4-3-teaching-by-example.md |
| 4-4 | How do you know your new prompt is better and not just different? | Every edit to a prompt feels like an improvement. A fixed set of hand-checked answers is the only thing that tells you when it isn't. | ${CLAUDE_PLUGIN_ROOT}/notes/4-4-better-or-just-different.md |

### Cluster 5: RAG systems and enterprise knowledge workflows

| # | Note | What it covers | File |
|---|---|---|---|
| 5-1 | Why can't you just paste all the company's documents into the prompt? | It sounds like the obvious design, and it fails three different ways before the documents even fit. | ${CLAUDE_PLUGIN_ROOT}/notes/5-1-why-not-paste-everything.md |
| 5-2 | What is retrieval, and what is an embedding? | Search that matches words fails the moment someone phrases things differently. Search that matches meaning has to turn meaning into numbers first. | ${CLAUDE_PLUGIN_ROOT}/notes/5-2-retrieval-and-embeddings.md |
| 5-3 | Why must a knowledge agent sometimes refuse to answer? | A system that always has an answer will eventually give you a wrong one in a perfectly confident voice. | ${CLAUDE_PLUGIN_ROOT}/notes/5-3-why-refuse-to-answer.md |
| 5-4 | How do you measure a system that answers questions? | One accuracy number hides three different ways to be wrong. Grade them separately and you'll know what to fix. | ${CLAUDE_PLUGIN_ROOT}/notes/5-4-measuring-a-rag-system.md |

### Cluster 6: Agentic AI workflows and automation design

| # | Note | What it covers | File |
|---|---|---|---|
| 6-1 | What turns a chatbot into an agent? | The jump from answering to acting is small in code and enormous in consequences. | ${CLAUDE_PLUGIN_ROOT}/notes/6-1-chatbot-to-agent.md |
| 6-2 | Why does every agent need a budget? | A loop that costs a little per turn has no ceiling unless you build one. A budget turns a nasty surprise into a number you chose. | ${CLAUDE_PLUGIN_ROOT}/notes/6-2-why-agents-need-budgets.md |
| 6-3 | What is an approval gate, and where do you put one? | You can't ask a human to approve every step, and you can't let an agent do everything alone. The trick is knowing which steps cannot be taken back. | ${CLAUDE_PLUGIN_ROOT}/notes/6-3-approval-gates.md |
| 6-4 | What happens when you run it twice? | Everything you build will be run twice by accident. The only question is whether the second run quietly doubles your data. | ${CLAUDE_PLUGIN_ROOT}/notes/6-4-run-it-twice.md |
| 6-5 | Why does your agent need a harness of its own? | A harness is a program whose whole job is to distrust your system. Building one is the most employable skill in this course. | ${CLAUDE_PLUGIN_ROOT}/notes/6-5-build-your-own-harness.md |

### Cluster 7: The anatomy of an agent

| # | Note | What it covers | File |
|---|---|---|---|
| 7-1 | Where does an agent keep its state? | The model remembers nothing between calls. Everything it appears to know was put in front of it, again, by your program. | ${CLAUDE_PLUGIN_ROOT}/notes/7-1-where-does-an-agent-keep-its-state.md |
| 7-2 | What should the model not decide? | Every question you hand to a model costs money, takes time and can come back wrong. A surprising number of them never needed a model. | ${CLAUDE_PLUGIN_ROOT}/notes/7-2-what-the-model-should-not-decide.md |
| 7-3 | Why must data never give orders? | Any text your system reads can contain a sentence addressed to your model. Safety comes from how you build, not from asking nicely. | ${CLAUDE_PLUGIN_ROOT}/notes/7-3-data-is-not-instructions.md |
| 7-4 | What is a skill, and how does an agent learn your way of working? | A skill is a file of rules and real examples that an agent loads when the task matches. It is how taste gets passed on without retraining anything. | ${CLAUDE_PLUGIN_ROOT}/notes/7-4-what-is-a-skill.md |
| 7-5 | How does an agent remember yesterday? | Agent memory is files it writes and reads back. That makes it simple to build, and it makes stale memory a liability. | ${CLAUDE_PLUGIN_ROOT}/notes/7-5-how-does-an-agent-remember.md |
| 7-6 | When does one agent become several? | Splitting work across agents adds a cost, coordination. Pay it only when the split earns it. | ${CLAUDE_PLUGIN_ROOT}/notes/7-6-when-one-agent-becomes-several.md |

### Cluster 8: APIs, data pipelines and system integration

| # | Note | What it covers | File |
|---|---|---|---|
| 8-1 | What is an API, really? | Every useful AI system spends most of its life asking other programs questions. The rules for asking are older and simpler than you think. | ${CLAUDE_PLUGIN_ROOT}/notes/8-1-what-is-an-api.md |
| 8-2 | Why is real-world data always messier than the demo data? | A field can be present, well-formed and wrong. Data lies in layers, and each layer needs its own check. | ${CLAUDE_PLUGIN_ROOT}/notes/8-2-real-data-is-messy.md |
| 8-3 | What breaks when two systems quietly disagree? | Both systems pass their tests and the combination is still wrong. The bug lives in the assumption between them. | ${CLAUDE_PLUGIN_ROOT}/notes/8-3-when-two-systems-disagree.md |
| 8-4 | How does your agent plug into tools it has never seen? | APIs let programs talk, but every connection used to be custom-built. A shared protocol changed what one small team can ship. | ${CLAUDE_PLUGIN_ROOT}/notes/8-4-how-agents-share-tools.md |

### Cluster 9: AI governance, privacy, risk and guardrails

| # | Note | What it covers | File |
|---|---|---|---|
| 9-1 | What must the model never see? | Anything you put in a prompt has left the building. The safest data to protect is the data you never sent. | ${CLAUDE_PLUGIN_ROOT}/notes/9-1-what-the-model-must-never-see.md |
| 9-2 | How should a system fail? | The most expensive output a pipeline can produce is a green checkmark that isn't true. | ${CLAUDE_PLUGIN_ROOT}/notes/9-2-how-should-a-system-fail.md |
| 9-3 | Who approved that? Audit trails and the paper they leave | When an AI system gets something wrong, the first question is which rows it touched. A system that can't answer that has to redo everything. | ${CLAUDE_PLUGIN_ROOT}/notes/9-3-who-approved-that.md |

### Cluster 10: Systems that improve themselves

| # | Note | What it covers | File |
|---|---|---|---|
| 10-1 | Why doesn't the model learn from its mistakes? | The model you use today is the same model tomorrow, however many times it gets something wrong. The system around it is where learning happens, if you build it. | ${CLAUDE_PLUGIN_ROOT}/notes/10-1-why-the-model-never-learns.md |
| 10-2 | What is a decision trace, and why write down the why? | Logs tell you what your system did. A decision trace tells the next person why it was built that way, and that is the part nobody can reconstruct later. | ${CLAUDE_PLUGIN_ROOT}/notes/10-2-what-is-a-decision-trace.md |
| 10-3 | Should the agent be allowed to improve itself? | An agent can read its own track record and suggest what to change. Whether those suggestions take effect should never be up to the agent. | ${CLAUDE_PLUGIN_ROOT}/notes/10-3-should-the-agent-improve-itself.md |

### Cluster 11: Stakeholder communication and solution presentation

| # | Note | What it covers | File |
|---|---|---|---|
| 11-1 | How do you explain your system to someone who will never read the code? | The person who decides whether your system gets used will read one page. Here is the page. | ${CLAUDE_PLUGIN_ROOT}/notes/11-1-the-solution-memo.md |
| 11-2 | How do you present numbers people can check? | The strongest number you can show is the one the reader could reproduce. Sizing your claim to your evidence is a skill. | ${CLAUDE_PLUGIN_ROOT}/notes/11-2-numbers-people-can-check.md |
| 11-3 | How do you say \"it didn't work\"? | A clean account of a failure is worth more than a clean record. Here is a real one, written the way we write them. | ${CLAUDE_PLUGIN_ROOT}/notes/11-3-saying-it-didnt-work.md |

## The path

Mission-order reading list (the same list as the body of note 0-1):

- **Week 0:** 0-1 · 1-1 · 1-2 · 3-1 · 3-2 · 3-3 · 3-4
- **Warm-up:** 6-1 · 8-1
- **Project 1:** 1-3 · 2-1 · 2-2 · 4-1 · 4-2 · 6-2 · 7-1 · 7-2
- **Project 2:** 4-3 · 4-4 · 6-4 · 6-5 · 7-4 · 8-2 · 9-2 · 10-1 · 10-2
- **Project 3:** 5-1 · 5-2 · 5-3 · 5-4 · 7-3
- **Project 4:** 2-3 · 6-3 · 7-5 · 9-1 · 9-3
- **Capstone:** 7-6 · 8-3 · 8-4 · 10-3 · 11-2 · 11-3
- **Every project ends with:** 11-1

## How to use them

1. Find out which mission stage the learner is at (ask, or look for PREDICTION.md, the Mission column of COURSE_PROGRESS.md, and recent work). Surface the note from that stage's list that matches the problem they are having right now, not the whole list.
2. Open the file and teach from it. Read the note; do not answer from memory of the topic. Keep its analogy and its production story.
3. Always offer the note's two-minute experiment.
4. On request, re-explain the idea against the learner's own project, with a different analogy, as a quiz, or by arguing the opposite side.
5. Never edit the note files.
