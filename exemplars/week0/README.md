> Rebuilt to the 2026-10-28 contract (BRIEF, PREDICTION, DECISIONS, TRACE_NOTES, `replies/`, `runs.txt` format, `.course/trace/`, `Model choice: b`). Real and untouched: the four calls and their traces, the replies, the prediction numbers and `POSTMORTEM.md`. Reconstructed from them afterwards: `BRIEF.md`, `DECISIONS.md`, `runs.txt` lines, `COURSE_PROGRESS.md`. Nothing here is replayed by a fake agent; `ask.py` is the real script and needs your own key to run again.

# Week 0 exemplar: first call, first trace

What is here, in the order to read it:

0. `BRIEF.md`, `DECISIONS.md`, `COURSE_PROGRESS.md` : the brief, the choices and the model option.
1. `PREDICTION.md` : written before the calls.
2. `ask.py` : the whole script. Standard library only.
3. `runs.txt` and `replies/run-1..4.txt` : one line per run, and the four replies.
4. `.course/trace/raw-calls.jsonl` : the real request and reply of each run.
5. `TRACE_NOTES.md` (five lines the mission asks for) and `TRACE_GUIDE.md` (how to read every field of that trace).
6. `POSTMORTEM.md` : what the prediction missed.
7. `hello.txt` : proof the agent can write files.

To run it yourself you need your own key, address and model name:

    export LLM_API_KEY=...   LLM_BASE_URL=...   LLM_MODEL=...
    python3 ask.py "In one sentence, what is a token?"
