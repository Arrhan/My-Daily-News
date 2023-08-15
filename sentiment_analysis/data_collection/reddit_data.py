#Data extraction for analysis
keywords =['OpenAI','Google','Microsoft','Amazon','Facebook','Twitter','Biden','Trump','Modi','Apple']
#Sources
sources = ['Reuters','Reddit','Twitter | Techcrunch']

#Reddit: posts and comments
import praw

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

data={}
subreddits=reddit.subreddit("news+technology+worldnews+politics+google+OpenAI+microsoft+amazon+twitter+india")


for keyword in keywords:
    submission_list = []
    #posts
    submissions = subreddits.search(keyword, sort='top', limit=15,time_filter='week')
    for submission in submissions:
        comments_list=[]
        #Comments
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if any(keyword.lower() in comment.body.lower() for keyword in keywords):
                comments_list.append(comment.body)
        #Post
        submission_dict = {
            'title': submission.title,
            'selftext': submission.selftext,
            'comments':comments_list
        }
        submission_list.append(submission_dict)
    data[keyword]=submission_list
print(data)

#How to access data dictionary:
##print(data['OpenAI'][0]['comments'][i])