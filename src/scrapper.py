import os
import re
from dotenv import load_dotenv
import praw

def load_credentials():
    load_dotenv()
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = os.getenv('REDDIT_USER_AGENT')
    return client_id, client_secret, user_agent

def clean_text(text):
    # Remove newlines and extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', text)

    # Remove Markdown formatting
    cleaned_text = re.sub(r'[*_~`]', '', cleaned_text)

    return cleaned_text

def scrape(reddit, subreddit_name, filepath):
    subreddit = reddit.subreddit(subreddit_name)

    # Scrape posts
    post_counter = 0
    print(f'Scraping posts from r/{subreddit_name}')
    
    with open(filepath, 'w', encoding='utf-8') as outfile:
        for post in subreddit.new(limit=None):
            post_title = clean_text(post.title)
            post_text = clean_text(post.selftext)

            outfile.write(f'{post_title}\n')
            outfile.write(f'{post_text}\n')
                       
            # Scrape comments for current post
            post.comments.replace_more(limit=None)
            comment_counter = 0
            for comment in post.comments.list():
                comment = clean_text(comment.body)
                outfile.write(f'{comment}\n')

                comment_counter += 1

            post_counter += 1
            print(f'Scrapped: Post #{post_counter} with {comment_counter} comments')

if __name__ == "__main__":
    subreddit_name = "nus"
    out_filepath = "../data/train.txt"

    client_id, client_secret, user_agent = load_credentials()
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        ratelimit_seconds=100
    )

    scrape(reddit, subreddit_name, out_filepath)