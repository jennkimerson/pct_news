# Reference: https://praw.readthedocs.io/en/latest/
# !pip install praw

import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='uFDD9nuv5yHZJA',
                     client_secret='wKIFKijChGdG0XJyuTB2UIV8XMo',
                     user_agent='pct_reddit_news')


# Get 10 new posts from the Boston_University subreddit
    # r/BostonU
    # Rhett-it: Boston University's unofficial Reddit community
new_posts = reddit.subreddit('BostonU').new(limit=10)
post_num = 1
for post in new_posts:
    print("Post Number: ", post_num, "\n")
    print("Post Title: ", post.title, "\n")
    submission = reddit.submission(id= post.id)
    submission.comments.replace_more(limit=0)
    print("Comments: ")
    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        print("== ", comment.body)
        for comment_replies in comment.replies:
            print("---", comment_replies.body)
    post_num += 1
    print("\n \n \n")


# Get subreddit data
    # Displays r/BostonU posting rules
# bu_subreddit = reddit.subreddit('BostonU')
# print(bu_subreddit.description)

# Save as CSV file
# import pandas as pd
# posts = []
# bu_subreddit = reddit.subreddit('BostonU')
# for post in bu_subreddit.hot(limit=10):
#     posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
# posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# print(posts)