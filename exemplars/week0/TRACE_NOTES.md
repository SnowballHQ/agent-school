1. First request: .course/trace/raw-calls.jsonl line 1, request.body.messages (also .course/trace/session-week0.jsonl line 1, role user)
2. Reply: .course/trace/raw-calls.jsonl line 1, response.body.choices[0].message.content (also .course/trace/session-week0.jsonl line 2)
3. Token counts: .course/trace/raw-calls.jsonl line 1, response.body.usage: 15 in, 35 out, 50 total (also .course/trace/session-week0.jsonl line 2 usage)
4. Moment the script ran: .course/trace/events.jsonl line 1, the ts and the python3 ask.py command
5. Stop reason: .course/trace/raw-calls.jsonl line 1, response.body.choices[0].finish_reason = stop (finished its thought; length would mean the 400 ceiling cut it off)
