# Hidden Markov Model

This project seeks to investigate more on Part-of-Speech (POS) tagging using Hidden Markov Model (HMM) with data taken from a subreddit.

For more information on POS tagging using HMM and Viterbi, do look at [Speech and Language Processing. Daniel Jurafsky & James H. Martin](https://web.stanford.edu/~jurafsky/slp3/A.pdf) for more details.

## Getting Started

All the source code can be found in `src/`. Ensure that you have installed the requirements listed in `requirements.txt`.

### Gathering Data

1. Create an `.env` file with following environment variables.

```txt
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=HS2914
SUBREDDIT_NAME=
```

2. Fill in `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` after [creating a new app on Reddit](https://www.reddit.com/prefs/apps/).

3. Fill in the `SUBREDDIT` to scrape through in `.env`.

4. Run `./src/scrapper.py`

### Preproceessing

This is done in 4 main steps:

1. Removing blank lines and trimming lines to remove trailing empty spaces
2. Remove hyperlinks
3. Remove `[deleted]` and `[removed]` tags
4. Remove file tags (i.e. `[img](img-url)`)

This is carried out by `./src/preprocess.py`.

### Creating our HMM and Performing Viterbi

For a detailed walkthrough, do look at `./src/hmm.ipynb`.
