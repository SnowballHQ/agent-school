# Brief

## What to build
A script `ask.py` that sends one question to my chosen model and prints the reply plus the tokens in and out. It also appends every call to `.course/trace/` so I can read it afterwards. Standard library only.

## Inputs and outputs
Input: one question on the command line, for example "In one sentence, what is a token?". The address, model name and key come from the environment variables `LLM_BASE_URL`, `LLM_MODEL` and `LLM_API_KEY`.
Output: the reply text, then a line `--- tokens in: N, out: N, total: N, seconds: S`. I run it four times: the same question three times (q=A), then a changed question once (q=B, "what is an API?"). Replies go in `replies/run-1.txt` to `run-4.txt`; one line per run goes in `runs.txt`.

## Must never happen
The secret key written into any file. The script writes `Bearer [REDACTED]` into the trace instead of the real header, and the key is only ever read from the environment. Reply length is capped at 400 tokens so a mistake cannot get expensive.

## Checks
Run `/agent-school:check week0`. Search the whole folder for the key's first characters after the runs and find nothing. Read `runs.txt` and confirm the three q=A rows have identical `in` and different `out`. Open the trace and find the stop reason myself.
