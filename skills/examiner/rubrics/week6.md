# Rubric: week6

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/7-week6.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Retrieval honesty**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Which unanswerable question was your agent most tempted to answer, and what stopped it?
2. How did you choose the refusal threshold, and on which questions?
3. Show me an answer whose citation is real but does not back the claim.
4. Did judging your own answers bias the correctness score? How would you reduce that?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- golden questions written after the retriever
- unanswerable questions that are trivially unrelated
- scores folded together into one number
- refusal left to the prompt with no code wall
- citation check stops at quote-exists
- learner judged answers while seeing the agent's confidence

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me a golden question set written (and committed) before the retriever.
2. Show me separate answer, citation and refusal scores.
