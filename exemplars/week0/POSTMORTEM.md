# Postmortem

## Predicted versus actual

| Prediction | I said | Actual | Verdict |
|---|---|---|---|
| Tokens, in and out | about 50 (12 in, 35 out) | 50 on run 1 (15 in, 35 out); 48 to 51 across the three | Right on the total, wrong on the split. |
| Identical replies out of 3 | 2 | 0 | Wrong. |
| Setup minutes | 20 | about 5 for the script and first call, plus one stumble | See below. |

My parts added to 47 and I rounded to "about 50", so the total looks right. But the input was 3 tokens off (12 guessed, 15 actual) and the output happened to land exactly on my guess of 35, which on a second run (36) or third (33) it would not have. Treat the total as partly luck. The input count is the lesson: a nine-word question cost 15, because each message carries a few tokens of wrapper that you never typed.

## What the prediction missed

1. **Identical replies.** I expected the model to repeat itself on a short question with one obvious answer. It did not, even once: "small unit", "unit", "discrete unit". Short and obvious does not mean fixed. Nothing about the answer being easy makes it repeat. If I had designed a check that compared replies for equality, it would have failed three times out of three.
2. **The wrapper.** I counted words and assumed words are tokens. 9 words became 15 tokens.
3. **Output size varies run to run** (33, 35, 36), so the cost of one call is a range, not a number.

## What went wrong in the build

- I tried to load the project's environment file straight into my shell and it stopped with a parse error on one line, because a value containing an `&` was not quoted. The keys I needed had loaded before the error, so the calls worked, but this is a real beginner trap: values with special characters need quotes in these files.
- Before writing this prediction I made one throwaway 23-token call to check the key worked. That call is not in the trace. It did not change my guesses, but a stricter reading of "write it before you run anything" says it should have waited.
- The setup-time number is the weakest part of this exemplar. I am an agent working in a prepared folder, so five minutes tells you nothing about your first evening. Expect 30 to 90 minutes, most of it on getting a key and an account working, none of it on code.

## The one sentence that goes in your own file

I predicted two identical replies in three; I got none, and the cost was fixed by the input to the call while the output moved by a few tokens every time.
