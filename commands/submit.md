---
description: Optional - share a finished mission as a public portfolio issue
---

Plugin files live under `${CLAUDE_PLUGIN_ROOT}` (an environment variable set by Claude Code); read them with the Read tool using that absolute path, never search the filesystem.

Submitting is optional and not needed for anything else in the course: feedback is local (`/agent-school:defend`), and the issue is a portfolio record in the public repo SnowballHQ/agent-school-submissions (anyone can read it). Say this once, then, if they still want to, submit the learner's mission. Work through the steps in order and stop at the first failure, explaining what to fix. Do not change the learner's files yourself beyond the trace staging below.

1. **Check the repo.** Run `git status --porcelain` and `git rev-parse HEAD`. Require a committed HEAD and a README in the repo root. Uncommitted changes outside `.course/trace/` mean the learner must commit or stash them first. If the README is missing, say so and help them see what it should state (see the mission brief); do not write it for them.
2. **Run the local check if the mission has one.** Run `/agent-school:check` for the mission if it has checks and show the result; a failing check is a reason to pause and ask whether to submit anyway. If none exists, say so and move on.
3. **Collect the facts.** Mission id (ask or read `COURSE_PROGRESS.md`: week0, warmup, project1, week2 to week8), repo URL (`git remote get-url origin`, converted to https form), full HEAD SHA and its first 7 characters. Ask the learner for optional Notes.
4. **Traces travel inside the repo.** Tell the learner plainly: submitting shares `.course/trace/` with anyone who can read the public issue's repo link, and the traces travel only because they are committed to the repo you link. If the repo is private, nothing is readable. Show what is there (`ls -la .course/trace/`, file count and size) and offer to open any file. Then ask for confirmation to stage ONLY `.course/trace/` additions: `git add .course/trace/` followed by a commit such as "Add course traces". Never stage anything else. If the learner declines, say that the submission can still be opened without the traces, and that they can delete them with `rm -rf .course/trace` first. Re-read the HEAD SHA after any commit, and check the commit is pushed (`git status -sb`); ask to push if not.
5. **Open the submission.** Title: `[<mission>] <repo>@<short-sha>`. Body:

   ```
   Mission: <mission id>
   Repo: <repo url>
   Commit: <full sha>
   Notes: <notes or "none">
   ```

   If `gh` is available and authenticated, run `gh issue create --repo SnowballHQ/agent-school-submissions --title "<title>" --body "<body>"` and show the issue URL. If `gh` is missing or not logged in, print a prefilled link instead: `https://github.com/SnowballHQ/agent-school-submissions/issues/new?title=<url-encoded title>&body=<url-encoded body>`, and tell the learner to open it and press Submit.
6. **Stamp the progress file.** In `COURSE_PROGRESS.md`, put the issue URL in the notes column of the mission's row (create the file with the `/agent-school:setup` steps if missing). Do not change the status.
7. **Close.** Confirm what was shared, and remind them how to delete traces locally: `rm -rf .course/trace`. Do not promise outcomes or timelines: feedback on your thinking is local, via `/agent-school:defend`, and the issue is a portfolio record.
