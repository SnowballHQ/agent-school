# Prediction (written before the first call)

Wrong numbers cost nothing. Unwritten numbers teach nothing.

## Predictions
1. How many tokens will my one question use, in and out together? My question is "In one sentence, what is a token?" That is 9 words, so about 12 tokens going in, and I expect a one-sentence answer of about 25 words, so about 35 coming out. Guess: **about 50 tokens in total.**
2. If I run the same question three times, how many replies will be word-for-word identical? The question is short and has one obvious answer. Guess: **2 of the 3 identical**, one slightly reworded.
3. How many minutes will setup take me? The script is small, but I have to find the key, learn the shape of the request, and fix at least one typo. Guess: **20 minutes.** (The mission's current third prediction asks instead whether the changed question will use more or fewer tokens; I did not make that prediction, and the gap section says what the measured numbers show.)

## The gap
1. Total tokens: 50 on run 1 (15 in, 35 out), 48 to 51 across the three same-question runs. Right on the total, wrong on the split: I guessed 12 in and got 15 because each message carries a few tokens of wrapper.
2. Identical replies: I said 2 of 3, the answer was 0 of 3 ("small unit", "unit", "discrete unit"). Short and obvious does not mean fixed.
3. Setup time: about 5 minutes plus one stumble, but an agent in a prepared folder tells you nothing about your first evening. On the changed question I made no prediction; it used 43 tokens (15 in, 28 out), 7 fewer than run 1, because the answer happened to be shorter while the input count stayed 15.

Full table and lessons: `POSTMORTEM.md`.
