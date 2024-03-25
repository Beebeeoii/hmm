# Hidden Markov Model

This project seeks to investigate more on Part-of-Speech (POS) tagging using Hidden Markov Model (HMM) with data taken from a subreddit.

## Getting Started

All the source code can be found in `src/`.

### Gathering Data

1. Make a copy of `.env.example` and rename it to `.env`

2. Fill in `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` after [creating a new app on Reddit](https://www.reddit.com/prefs/apps/).

3. Fill in the `SUBREDDIT` to scrape through in `.env`.

4. Run `./scrapper.py`

### Preproceessing

The preprocessor removes blank lines, hyperlinks, file_uploads, `[removed]` and `[deleted]` posts/comments.
It can be accessed via `./preprocess.py`.
