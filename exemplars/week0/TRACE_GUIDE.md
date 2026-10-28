# Reading the trace (full field guide; the five-line TRACE_NOTES.md is the mission deliverable): every field, in the order you meet it

Files in `.course/trace/`:

- `raw-calls.jsonl` is the exact request and reply of each call, one call per line. Read this first.
- `session-week0.jsonl` is the same four calls in the course plugin's session format: one line per message, with who said it and what it cost.
- `events.jsonl` is one line each time the script was run (the plugin writes the same kind of line each time your agent runs a command).

Two honest notes. This trace was written by `ask.py` itself, in the plugin's format, because no agent session was recording. Your own trace will be written by the plugin and will also hold your agent's conversation. And I replaced the service's web address and the model's name with `<provider-host>` and `<model-id>`; everything else is untouched.

Line 1 of `raw-calls.jsonl`, field by field.

## The request (what you sent)

| Field | Value | How to read it |
|---|---|---|
| `ts` | `2026-10-10T13:29:37+00:00` | When the call was logged. `+00:00` means universal time, not your clock. |
| `seconds` | `1.58` | How long you waited, from sending to getting the full reply. |
| `request.method` | `POST` | "I am sending you something", as opposed to just asking to look at a page. |
| `request.url` | `.../v1/chat/completions` | The address of the one door that takes questions. |
| `headers.Authorization` | `Bearer [REDACTED]` | Your secret key. The script wrote `[REDACTED]` into the trace on purpose. A trace you cannot share safely is a trace you will stop saving. |
| `headers.Content-Type` | `application/json` | "The body below is JSON." |
| `body.model` | `<model-id>` | Which model you are renting. The same question to a different model gives a different answer and a different bill. |
| `body.messages` | one entry, `role: user` | The conversation so far. Here it is one message, yours. In an agent this list grows with every step, and you pay for all of it each time. |
| `body.max_completion_tokens` | `400` | A ceiling you set on the reply. If the model ran on, it would be cut at 400 tokens. This is your first budget. |

## The reply (what came back)

| Field | Value | How to read it |
|---|---|---|
| `response.status` | `200` | "It worked." Anything else (401 wrong key, 429 too many requests, 5xx their fault) means there is no answer to read. |
| `body.id` | `chatcmpl-...` | A label for this one call. Quote it if you ever need to ask the provider what happened. |
| `body.created` | `1791638976` | When the service made the reply, as seconds since 1 January 1970. |
| `body.model` | `<model-id>` | The model that actually answered. Check it matches the one you asked for. |
| `choices[0].message.content` | "A token is a small unit of text..." | The answer. There is a list of choices because you can ask for several; you asked for one. |
| `choices[0].message.refusal` | `null` | Filled in only if the model declined. |
| `choices[0].finish_reason` | `stop` | Why it stopped writing. `stop` means it finished its thought. `length` would mean your 400 ceiling cut it off mid-sentence. Always look at this. |
| `usage.prompt_tokens` | `15` | Tokens you sent. Your question is 9 words, yet it cost 15: the message wrapper (who is speaking) costs tokens too. |
| `usage.completion_tokens` | `35` | Tokens it wrote. This is the number that grows if you ask for more. |
| `usage.total_tokens` | `50` | In plus out. This is what you are billed on (output usually at a higher price per token than input). |
| `prompt_tokens_details.cached_tokens` | `0` | Input the service had seen recently and charges less for. Zero on a short, fresh question. |
| `completion_tokens_details.reasoning_tokens` | `0` | Tokens the model spent thinking before answering. Zero here. On harder questions this can be most of the bill, and you do not see it. |

The remaining fields (`service_tier`, `system_fingerprint`, `annotations`, the `*_prediction_tokens` and `audio_tokens`) were empty or zero; skip them until one is not.

## The four things the mission asks you to find

1. **Your first request:** line 1 of `raw-calls.jsonl`, under `request.body.messages`. Also line 1 of `session-week0.jsonl`, `role: user`.
2. **The model's reply:** the same line, `response.body.choices[0].message.content`. Also line 2 of `session-week0.jsonl`, `role: assistant`.
3. **The token counts:** `response.body.usage` (three numbers). Also `usage` on the assistant line of `session-week0.jsonl`.
4. **The moment your script ran:** line 1 of `events.jsonl`, the `ts` and the `command` that was typed.

## What the four calls show side by side

| Run | Question | In | Out | Seconds |
|---|---|---|---|---|
| 1 | what is a token | 15 | 35 | 1.58 |
| 2 | what is a token | 15 | 36 | 1.34 |
| 3 | what is a token | 15 | 33 | 1.24 |
| 4 | what is an API | 15 | 28 | 1.28 |

Same question, three different sentences ("small unit", "unit", "discrete unit") and three different output counts. The input count is identical every time because the input did not change. Only the output is chosen by chance. That is the whole of note 3-4 in one table.
