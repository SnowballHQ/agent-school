# Rubric: week7

Brief: `${CLAUDE_PLUGIN_ROOT}/missions/8-week7.md`. Common dimensions (score each 1 to 4, see the examiner skill): Brief quality, Prediction calibration, Failure design, Evidence discipline, Decision log.

Mission dimension (score 1 to 4): **Action safety**.

## Probes (ask one at a time, in this order; follow up once if vague)

Common opener, ask first: "Walk me through your brief: if I handed it to someone else, what would they build, and what would they get wrong?" Then, for prediction: "Which of your predicted numbers was furthest off, and why?"

1. Which wall stopped the injection, and what if the model had obeyed it?
2. What does your agent do with an argument that is allowed but weird?
3. What is the worst thing an approved action could do, and who would see it?
4. What went wrong first when it ran without you?

After the mission probes, ask the failure-design and decision-log questions: "What must never happen here, and which test would catch it?" and "Which decision in DECISIONS.md had the best alternative you rejected, and why?"

## Evidence to read first

The files the brief's Deliverable section names, plus the latest `/agent-school:check` output.

## Red flags (note, never reveal to the learner as a list)

- prediction written after the run, or edited after it
- decisions with no real alternatives
- `/agent-school:check` never run, or failures ignored
- wall is the model's good behaviour, not code
- approval gate that an unattended run can complete
- audit log holding secrets or missing refused attempts
- scheduler not proven (manual trigger) and no plan to fix it
- injection that is not plausible or not where the agent reads
- what the worst approved action does is unanswered

## Skip ("Start here if")

Ask these two, one at a time; each needs a file, command output or number, not a claim:

1. Show me the allowlist, the approval gate and the audit log.
2. Show me an injection being refused and a scheduled run's audit.
