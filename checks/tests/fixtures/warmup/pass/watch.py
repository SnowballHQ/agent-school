import json, sys, os
args = sys.argv[1:]
state_path = args[args.index("--state") + 1] if "--state" in args else "state.json"
here = os.path.dirname(os.path.abspath(__file__))
board = json.load(open(os.path.join(here, "board.json")))
now = "2026-10-28T00:00:00Z"
state = json.load(open(state_path)) if os.path.exists(state_path) else {"meta": {}, "postings": {}}
posts = state["postings"]
lines = []
seen = set()
for j in board:
    slug = j["slug"]; seen.add(slug)
    if slug not in posts:
        posts[slug] = {"title": j["title"], "first_seen": now, "last_seen": now, "gone_at": None}
        lines.append("new: %s | %s" % (slug, j["title"]))
    elif posts[slug]["gone_at"]:
        posts[slug]["gone_at"] = None
        lines.append("returned: %s | %s" % (slug, j["title"]))
for slug, v in posts.items():
    if slug not in seen and not v["gone_at"]:
        v["gone_at"] = now
        lines.append("gone: %s | %s" % (slug, v["title"]))
if lines:
    state["meta"] = {"fetched": len(board), "complete": True}
    json.dump(state, open(state_path, "w"), indent=2, sort_keys=True)
    print("\n".join(sorted(lines)))
else:
    print("nothing new")
