#!/usr/bin/env bash
# Pipes fixture hook payloads into trace.py and asserts on the output files.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
TRACE="$HERE/../trace.py"
W="$(mktemp -d)"; trap 'rm -rf "$W"' EXIT
fail=0
ok(){ echo "PASS $1"; }
bad(){ echo "FAIL $1"; fail=1; }
check(){ if eval "$2"; then ok "$1"; else bad "$1"; fi; }
feed(){ sed -e "s#@CWD@#$1#g" -e "s#@T@#$HERE/transcript.jsonl#g" "$HERE/$2" | python3 "$TRACE"; echo $?; }

mkdir -p "$W/course/.course" "$W/plain"
# 1. guard: no .course => nothing written, exit 0
rc=$(feed "$W/plain" post_tool_use_bash.json)
check "no .course: exit 0" '[ "$rc" = 0 ]'
check "no .course: nothing written" '[ ! -e "$W/plain/.course" ]'
# 2. PostToolUse
feed "$W/course" post_tool_use_bash.json >/dev/null
feed "$W/course" post_tool_use_write.json >/dev/null
E="$W/course/.course/trace/events.jsonl"
check "events: 2 lines" '[ "$(wc -l < "$E")" -eq 2 ]'
check "events: bash command kept, bearer scrubbed" 'grep -q "Bearer \[REDACTED\]" "$E" && ! grep -q abcdef1234567890 "$E"'
check "events: API_KEY value scrubbed" '! grep -q zzz123 "$E"'
check "events: write keeps file_path only" 'grep -q "/x/agent.py" "$E" && ! grep -q BIGBODY "$E"'
# 3. Stop
feed "$W/course" stop.json >/dev/null
S="$W/course/.course/trace/session-s1.jsonl"
check "session: 4 messages" '[ "$(wc -l < "$S")" -eq 4 ]'
check "session: secrets scrubbed" '! grep -Eq "sk-ant-api03|hunter2|AKIAABC|abcdef1234567890" "$S"'
check "session: usage + model present" 'grep -q "\"output_tokens\": 40" "$S" && grep -q claude-sonnet-5-5 "$S"'
check "session: cursor = 5" '[ "$(cat "$W/course/.course/trace/.cursor-s1")" = 5 ]'
# 4. idempotent second Stop, then incremental append
feed "$W/course" stop.json >/dev/null
check "rerun adds no duplicates" '[ "$(wc -l < "$S")" -eq 4 ]'
cp "$HERE/transcript.jsonl" "$W/t2.jsonl"
echo '{"type":"assistant","message":{"role":"assistant","model":"m","content":"more","usage":{"input_tokens":1,"output_tokens":2}}}' >> "$W/t2.jsonl"
sed -e "s#@CWD@#$W/course#g" -e "s#@T@#$W/t2.jsonl#g" "$HERE/stop.json" | python3 "$TRACE"
check "incremental: only new message appended" '[ "$(wc -l < "$S")" -eq 5 ]'
# 5. garbage never crashes
echo 'not json' | python3 "$TRACE"; check "garbage stdin: exit 0" '[ $? = 0 ]'
echo '{"cwd":"'"$W/course"'","hook_event_name":"Stop","session_id":"s9","transcript_path":"/nope"}' | python3 "$TRACE"
check "missing transcript: exit 0" '[ $? = 0 ]'
exit $fail
