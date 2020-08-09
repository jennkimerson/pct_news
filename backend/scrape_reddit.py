# Reference: https://praw.readthedocs.io/en/latest/
# !pip install praw

from pymongo import MongoClient
import praw
from praw.models import MoreComments

# Mongodb Connection
client = MongoClient("mongodb+srv://test:test@cluster0.zp7va.mongodb.net/reddit_db?retryWrites=true&w=majority")
db = client.get_database('reddit_db')
scrape = db.post_scrape
# scrape.count_documents({})


# Get 10 new posts from the Boston_University subreddit
# r/BostonU
# Rhett-it: Boston University's unofficial Reddit community

reddit = praw.Reddit(client_id='uFDD9nuv5yHZJA',
                     client_secret='wKIFKijChGdG0XJyuTB2UIV8XMo',
                     user_agent='pct_reddit_news')


# Posts
new_posts = reddit.subreddit('BostonU').new(limit=3)
post_num = 1
for post in new_posts:
    reddit_post = {
        'Post Number': post_num,
        'Post ID': post.id,
        'Post Title': post.title,
        'Post content': post.selftext
        # 'Comments': []
    }
    print(reddit_post)

    # Comments
    # submission = reddit.submission(id=post.id)
    # submission.comments.replace_more(limit=None)
    # comment_thread = []
    # for comment in submission.comments.list():
    #     reddit_comment = {
    #         'Post ID': post.id,
    #         'Comment': submission.comments
    #     }
    #     print(comment)
        # comment_thread.append(comment)
    # print(reddit_comment)

        # Sub-comments
        # if isinstance(comment, MoreComments):
        #     continue
        # New array, append comment_replies
        # for sub_comment in comment.replies:
        #     reddit_post.update({'Comments': sub_comment.body})
    post_num += 1
    scrape.insert(reddit_post)

# Make comments their own MongoDB objects, have reference to the parent - pair with object ID

# Print Statements
# new_posts = reddit.subreddit('BostonU').new(limit=2)
# post_num = 1
# for post in new_posts:
#     print("Post Number: ", post_num, "\n")
#     print("Post ID: ", post.id, "\n")
#     print("Post Title: ", post.title, "\n")
#     print("Post Content: ", post.selftext, "\n")
#     submission = reddit.submission(id=post.id)
#     submission.comments.replace_more(limit=0)
#     print("Comments: ")
#     for comment in submission.comments.list():
#         if isinstance(comment, MoreComments):
#             continue
#         print("== ", comment.body)
#         for comment_replies in comment.replies:
#             print("---", comment_replies.body)
#     post_num += 1
#     print("\n \n \n")


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
