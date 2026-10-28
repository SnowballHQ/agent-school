# Rubric: warmup

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/1-warmup.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Idempotence and who decides**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Why this key, and what happens to your memory when a posting disappears and returns?
2. Which part does the model decide, and why not the diff? What did your second run cost?
3. How narrow is your watch, and how do you know you read it all?
4. What did the staged change show that the plain second run could not?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- the model is doing the diff (cost > 0 on a no-change run)
- second run output not exactly `nothing new` and the learner shrugs
- watch truncated at the page limit rather than narrowed
- no staged change run; learner cannot say what it proved
- decisions with no alternatives (key, gone handling)
- prediction written after the run

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me an agent with a memory file.
2. Show me the diff (or hashes) proving its second run changed nothing.
