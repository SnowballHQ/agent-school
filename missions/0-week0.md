---
title: "Week 0: set up, make your first call, read a trace"
access: free
---
# Week 0: set up, make your first call, read a trace

Free tier. One sitting, about two hours. No portfolio value; this one makes everything after it possible.

## The three ideas you need

You do not have to have read anything first. These three are enough to start.

1. **A model predicts text, and you pay for it by the token.** A **model** is a program that reads text and writes the most likely continuation. A **token** is a small chunk of text, roughly three quarters of a word, and it is the unit you are measured and billed in. Everything you send in and everything you get back is counted. Field notes: "What is a model actually doing when it answers you?" and "What are tokens, and why does anyone count them?"
2. **An API is a contract for asking a program to do something.** An **API** is a fixed way to send a request to another program and get a predictable reply. Your first call will be one request out, one reply back, nothing more. Field note: "What is an API, really?"
3. **A trace is the record of what happened.** A **trace** is a log of every step a run took: what was sent, what came back, what it cost, how long it took. Models give different answers to the same question, so you cannot rerun your memory of what happened. You read the trace instead. Field note: "Why does the same question get different answers?"

## The mission

You will do three things, in order.

1. **Set up your environment.** Install the course plugin, open a fresh folder for your work, and run the enroll command so your folder knows who you are. Then check that a `.course` directory now exists in that folder (`ls -a`). The plugin saves your trace there, and without it step 3 has nothing to read; if it is missing, run the enroll command again from inside the folder. Confirm that your coding agent can read and write files in that folder. If you can create a file called `hello.txt` by asking for it, setup is done.
2. **Make your first API call.** Write a small script that sends one question to a frontier model and prints the reply and the number of tokens used. Run the same question three times, saving each reply and token count. Then change the question and run it once more. Notice that the three replies to the same question differ from each other, and that the token counts differ too.
3. **Read a trace.** The plugin saves a trace of your session into your folder. Open it and find four things: your first request, the model's reply, the token counts, and the moment your script ran. Write four lines in `TRACE_NOTES.md`, one per item, saying where you found each.

## Deliverable and how it's checked

Your folder contains:

- `hello.txt`, proving the agent can write files.
- Your script, plus the output of the three same-question runs and the one changed-question run saved to `runs.txt`.
- `TRACE_NOTES.md` with four lines, each pointing to a real spot in the trace.
- `PREDICTION.md`, written before you made the call (see below).

The check is mechanical. The harness opens your trace and confirms it is readable: valid, nonempty, with at least one request and one reply in it. A mentor reads `TRACE_NOTES.md` and checks that the four spots you named exist. Nobody grades the quality of your script.

## Predict before you build

Write these in `PREDICTION.md` before you run anything. Wrong numbers cost nothing. Unwritten numbers teach nothing.

1. How many tokens will your one question use, in and out together?
2. If you run the same question three times, how many of the three replies will be word-for-word identical?
3. How many minutes will setup take you?

After the third run, add one sentence per prediction saying what actually happened.

## When you're stuck

- Run `/mission` and your mentor will find which step you are on and continue from there.
- Run `/notes 3-2` (or any note number above) to have the mentor re-teach that note against what is on your screen right now.
- Notes to reach for: 3-1, 3-2, 3-4, 8-1.
- Permission slip for the cohort channel: "I got stuck at this step, here is what I tried and what I saw." That sentence is a complete, welcome post.
