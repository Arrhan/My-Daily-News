import praw
import pandas as pd

client_id = "34nmqpP4jMviHnP42jrSFw"
client_secret = "1kDyV5593u6sh__od4HcUZ8CXCBy_A"
user_agent = "changpop"
password = "Foot@1910ball"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    password=password,
    username=user_agent
)

#Getting top posts (greater than 1k upvotes) in last 24 hours from r/news and r/technology
rnews= reddit.subreddit("news+technology+worldnews")
top_rnews = rnews.top(time_filter='day')
minimum_upvotes = 1000
top_news_posts = []

for post in top_rnews:
    if post.ups >= minimum_upvotes:
        top_news_posts.append(post.url)

#r/politics (greater than 5k upovtes)
rpolitics = reddit.subreddit("politics")
top_rpolitics = rpolitics.top(time_filter='day')
politics_upovtes = 7000

politics=[]
for post in top_rpolitics:
    if post.ups >= politics_upovtes:
        top_news_posts.append(post.url)

# CONVERT LIST TO DATABASE format
top_news_posts=pd.DataFrame(top_news_posts)