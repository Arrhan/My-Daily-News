import http.client, urllib.parse
import datetime
import reddit
import google_trends
import pandas as pd

pd.set_option('display.max_colwidth', None)

#Reddit news
print("Top News from reddit:")
print(reddit.top_news_posts)
print('\n')

#Setting dates to get news articles from last 24 hours
current_date = datetime.datetime.today().strftime ('%Y-%m-%d')

previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
previous_date=previous_date.strftime ('%Y-%m-%d')

#KEYWORDS OF INTEREST ------
economy = 'inflation OR government OR stock market OR recession OR rally OR job market '
business = 'OR Venture Capital OR Investment OR startups OR Morgan OR BlackRock OR Meta OR Facebook OR NASA OR Tesla OR SpaceX OR Apple OR Microsoft OR Amazon OR Nvidia OR Google OR Twitter OR X '
technology = 'OR Bill Gates OR Zuckerberg OR Musk OR ChatGPT OR A.I. OR artifical intelligence OR machine learning OR software OR hardware OR DeepMind OR Chips OR Jeff Bezos  OR electric vehicles OR Larry Bird OR Brin OR chatbot OR OpenAI '
politics = 'OR Republicans OR GOP OR G.O.P. OR Biden OR Democrats OR Modi OR Jinpeng OR elections '
other = 'OR global warming OR heat OR university OR college admissions OR Obama'
trend_topics = ''
trending_tech_topics=''

#Adding google trends to trending_topics
for i in range(0,15):
    trend_topics+=google_trends.trending_topics[0][i] + " OR "
trending_topics=str(trend_topics)+'researchers'
#Adding tech_search keywords to tech_topics
tech_topics=''
if len(google_trends.tech_searches)<15:
    for i in range(0,len(google_trends.tech_searches)):
        tech_point=google_trends.tech_searches['title'][i].replace(", "," OR ")
        tech_topics+=tech_point+" OR "
else:
    for i in range(0,15):
        tech_point=google_trends.tech_searches['title'][i].replace(", "," OR ")
        tech_topics+=tech_point+" OR "

tech_topics=str(tech_topics)+"scientist OR scientists"

#Final list of topics to sift for news articles REMOVE LAST OR FROM trending_topics
main_topics = economy+technology+business+politics+other

#MAIN ARTICLES ------
conn = http.client.HTTPConnection('api.mediastack.com')

params_main = urllib.parse.urlencode({
    'access_key': '78bacb491fd29aad5689fd3809353ba9',
    'keywords': main_topics,
    'sources': 'cnn,nytimes',
    'sort':'popularity',
    'date': previous_date,
    'limit': 45
    })

conn.request('GET', '/v1/news?{}'.format(params_main))

res = conn.getresponse()
data = res.read()
articles = data.decode('utf-8')

print("Main articles:")
print(articles+'\n')
print("Articles on trending topics:")

#TREND ARTICLES -----
params_trend = urllib.parse.urlencode({
    'access_key': '78bacb491fd29aad5689fd3809353ba9',
    'keywords': trend_topics,
    'sources': 'cnn,nytimes',
    'sort':'popularity',
    'date': previous_date,
    'limit': 45
    })
conn.request('GET', '/v1/news?{}'.format(params_trend))

res = conn.getresponse()
data = res.read()
trending_articles = data.decode('utf-8')
print(trending_articles+'\n')

print("Articles on trending tech topics:")

#TREND TECH ARTICLES ------
params_tech = urllib.parse.urlencode({
    'access_key': '78bacb491fd29aad5689fd3809353ba9',
    'keywords': str(tech_topics),
    'sources': 'cnn,nytimes',
    'sort':'popularity',
    'date': previous_date,
    'limit': 45
    })
conn.request('GET', '/v1/news?{}'.format(params_tech))

res = conn.getresponse()
data = res.read()
trending_tech_articles = data.decode('utf-8')
print(trending_tech_articles)