# Brief defects found while executing the briefs

QA harvest from building the Week 0, Warm-up and Project 1 exemplars. Ordered most damaging first inside each brief. Quotes are exact.

## Top three

1. **Warm-up: the check cannot be run as written.** "Take a snapshot of your memory file and output, run again, snapshot again, and compare. The diff must be empty." The second run's output is "nothing new" and the first run's is a full list, so the two outputs can never diff empty. Only the memory file can. Say "diff the memory file; the second run's output must read exactly 'nothing new'."
2. **Project 1: "Interview one real person about the work. Quote them." has no fallback.** An exemplar builder, or any learner without access to a practitioner in their vertical, cannot satisfy step 1, and the clinic criterion depends on it. Decide: is a stand-in quote allowed (marked as such), or is a real interview a hard gate? Related: "Run it on at least twenty postings" but the reviewed sample size is never stated; I chose 15 and had to guess.
3. **Project 1: "Heading five must be a concrete example" does not say the example has to change the design, yet the clinic does.** "the 'must never happen' line changes at least one design decision you can point to". My first guard (check the quote exists) satisfied the clinic and still missed both real failures. Tell learners to test their guard on a posting built to beat it.

## Week 0 (`0-week0.md`)

- "Change the question and run it three times. Notice that the replies differ" versus prediction 2, "If you run the same question three times, how many of the three replies will be word-for-word identical?" One asks for different questions, the other for the same one. A learner who follows the first cannot answer the second. I ran the same question three times plus one changed.
- "Write four lines in `TRACE_NOTES.md`, one per item" versus the field-by-field reading an exemplar needs. Fine for a first pass, but it never asks the learner to find `finish_reason`, the single field that explained my warm-up failure. Consider a fifth line.
- "Install the course plugin, open a fresh folder ... run the enroll command" is step 1 of the mission but the trace "the plugin saves" only exists once a `.course` directory exists. `trace.py` does nothing without it, and the brief never says to create or confirm it. A learner can finish step 3 with an empty trace.
- "The harness opens your trace and confirms it is readable: valid, nonempty, with at least one request and one reply in it." The plugin trace holds the agent's conversation and tool events, not the learner's script's HTTP request. Which "request" and "reply" count? I could not tell, so my exemplar writes the plugin format itself.
- "sends one question to a frontier model": no word on where a free-tier learner gets a key, an address and a model name. All the cost lands here and the brief calls it free.
- "How many minutes will setup take you?" is not checkable for the builder (an agent) and says nothing about what counts as setup.

## Warm-up (`1-warmup.md`)

- "Choose your watch: one search, such as a role family plus a seniority plus a location rule". The tool's own description says to ask the user their country, and `geo` has a rule that only India-based users pass `india_ok`. The brief never tells the learner to read that, though step 1 says to read each description.
- "Fetch matching jobs." Fetch how many? The search returns 50 per page. A watch over 100 postings needs paging, and a watch cut short by a page limit makes old postings fall off and look "gone". The brief should say a watch too wide to read fully must be narrowed, not truncated.
- "Report only postings that are new or gone. Then update the memory file." What happens to a "gone" posting's key afterwards? If it stays in memory it is reported gone forever; if removed, a posting that disappears and returns is "new" again. Undefined.
- "Give every posting a key, a value that stays the same across runs, such as the posting's id." The search results carry `slug`; get_job takes `slug`; nothing is called "id". Name the field.
- "What will one full check cost, in tokens?" assumes the model reads the postings. A watch built right (code does the diffing) costs 0 tokens when nothing changed. The brief does not say whether the model must be in the loop at all; the three-ideas section says "An agent is a goal, some tools and a loop", which pushes learners to put the model in charge of the diff. Say which part the model should and should not decide (note 7-2).
- "If the board changes between your two runs, how many new postings do you expect to see?" Two runs a minute apart will almost never see a change, so the learner learns nothing about whether the agent can detect change. Add a staged-change step (I added one).
- "If a mentor or the harness finds even one repeated or reordered line". "Reordered" has no meaning if only the memory file is compared and it is keyed; say it applies to the file.
- Deliverable says the repo has "a README stating what you watch and how to run it" but never says what to do about the model key (where it lives, that it must not be committed).
- "Deployed publishes one at `https://deployed.so/mcp`": the exemplar had to speak to it with plain HTTP and a session header. A learner using a coding agent will not, but the brief does not say which client they are meant to use for the loop.

## Project 1 (`2-project1.md`)

- "Pick a vertical you know. Interview one real person about the work. Quote them." (see top three).
- "Count whether the problem is worth automating: volume, frequency, cost of the manual way." No threshold. Is 4 hours a month worth it? The grading line, "you will be graded on the evidence", never says what evidence is enough.
- "Heading four must be a test, such as 'ninety of a hundred reviewed rows match a human's answer.'" The brief then asks for a reviewed "sample" and never says who reviews it or how large it is. A review by the builder is not independent; mine was not.
- "Heading five must be a concrete example". One example or several? And does a number count ("zero wrong dates")?
- "outputs a JSON matching a schema you design, with fixed option lists wherever a field could drift (seniority, remote status)". Seniority and remote status are job-posting fields; in a burned domain the learner must invent the equivalents. Fine for them, but ranges like "intermediate and advanced" have no home in a single-value list. Tell learners to decide on the multi-value case up front.
- "Handle a non-matching answer by retrying once, then recording the failure". My agent never failed the schema, so the retry path ran zero times and is untested. Nothing in the brief asks for a deliberate test of it.
- "The harness validates every output file against your schema and reports the share that is valid. Version 0 passes when every file is valid JSON and every failure is recorded. Accuracy is measured later." So the harness never sees the wrong deadlines that matter. Either measure a "never happens" count at v0 or say plainly that v0 only proves format.
- "Which field will fail most often, and why?" is asked before the learner has labelled anything, and a field with only two distinct values cannot fail "most often" in a meaningful way. Say to predict after the schema is final.
- "`PREDICTIONS.md`, written before Part B" but the Week 0 and warm-up files are `PREDICTION.md` (singular). `/predict` creates `PREDICTION.md`. Pick one.
- Deliverable lists `RESULTS.md`; the design rules for the exemplar say POSTMORTEM. They are the same job. Pick one name.
- Prediction 2 asks cost for "one hundred" postings but the run is "at least twenty"; the extrapolation is a guess, and an hidden thinking budget (reasoning tokens, see Warm-up) can make it wrong by 2x. Mention that the usage field is the only honest cost.

## Packaging and tooling gaps outside the briefs

- `plugin/skills/warm-up-mission/SKILL.md` and `plugin/README.md` (line 17) still point at `missions/warm-up.md`. I left a "Moved" stub in `plugin/missions/warm-up.md` so they keep working; the skill should be repointed to `1-warmup.md`.
- `plugin-private/missions/p1.md` is still the old placeholder ("Research and enrichment agent"), which no longer matches the new Project 1 (extraction). `plugin-private/commands/mission.md` still lists warm-up, p1..p4, capstone and reads `./missions/<name>.md`; it knows nothing of `0-week0`, `1-warmup` or `2-project1`. I was told to repoint only the public `mission.md`.
- `plugin-private/commands/predict.md` writes `PREDICTION.md` and quotes the warm-up path `./missions/warm-up.md`.
- `/submit` leaves no local record that a mission was submitted, so `/exemplar` has to ask the learner for the issue link or query GitHub with `gh`. A one-line marker file written by `/submit` would make the gate checkable.
- `trace.py` records tool events and transcripts but never HTTP calls made by the learner's own script, so for Week 0 the "request" and "reply" in the trace are the agent's chat messages, not the API call. The exemplar's `raw-calls.jsonl` is not something the plugin produces.
- The board's vendor and model names appear in verbatim posting data (titles, skill tags, slugs) in the warm-up exemplar. I left them as data; the no-vendor-names rule is satisfied for prose only.
