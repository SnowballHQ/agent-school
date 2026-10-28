# Brief

## What to build
A watch on the Deployed remote-jobs board for one narrow search (senior ML/AI roles, remote or open to India), saved in `watch.json`. It reports only what changed since it last looked. The key is the posting's `slug`. Code does the diffing, not the model: a check where nothing changed costs zero tokens. A model may be used only for an optional verdict per new posting (`--summarise`).

## Inputs and outputs
Input: the board's `search_jobs` tool through the MCP server at `https://deployed.so/mcp` (or, for an offline run, saved pages via `--replay board_saved.json`), plus the memory file `state.json`, set with `--state <path>`.
Output: one line per change, `new: <slug> | <title>`, `gone: <slug> | <title>`, `returned: <slug> | <title>`, or the single line `nothing new`. Memory: `{"meta": {"fetched": N, "complete": true}, "postings": {"<slug>": {"title", "first_seen", "last_seen", "gone_at"}}}`; a vanished posting keeps its key and gets `gone_at`. Model credentials live in environment variables, never in a file.

## Must never happen
A half-read list marking unread postings as `gone`: if the search cannot be read fully (more than 4 pages or a failed fetch) the run stops before touching memory. Also: comparing by list position, the memory file changing on a run that found nothing, and a model call when nothing changed.

## Checks
Run twice: the second run prints exactly `nothing new` and `state.json` is byte-identical (`diff-live-run.txt`). Stage a change: delete one key from a copy of the memory file and run with `--state <copy>`; exactly one `new:` line appears. `usage.jsonl` does not grow on the second run. `/agent-school:check warmup`.
