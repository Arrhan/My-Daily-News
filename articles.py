import http.client, urllib.parse
import datetime
import reddit
import google_trends
import pandas as pd
import json
import re

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

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
for i in range(0,20):
    tech_point=google_trends.tech_searches['title'][i].replace(", "," OR ")
    trending_tech_topics+=tech_point+" OR "

tech_topics=str(trending_tech_topics)+"scientists"

#Removing all non alphanumer chaarcters except space for tech_topics and trending_topics to ensure compatible with keyword functionality
tech_topics = re.sub(r'[^A-Za-z0-9. ]+', '', tech_topics)
trending_topics = re.sub(r'[^A-Za-z0-9. ]+', '', trending_topics)

#Final list of topics to sift for news articles
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
#Converting JSON output to pandas dataframe
parsed_data = json.loads(articles)
article_data = parsed_data["data"]
df = pd.DataFrame(article_data)
print(df)

print("Articles on trending topics:")

#TRENDING ARTICLES -----
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

parsed_data = json.loads(trending_articles)
article_data = parsed_data["data"]
df = pd.DataFrame(article_data)
print(df)

print("Articles on trending tech topics:")

#TRENDING TECH ARTICLES ------
params_tech = urllib.parse.urlencode({
    'access_key': '78bacb491fd29aad5689fd3809353ba9',
    'keywords': tech_topics,
    'sort':'popularity',
    'sources': 'cnn,nytimes',
    'date': previous_date,
    'limit': 45
    })
conn.request('GET', '/v1/news?{}'.format(params_tech))

res = conn.getresponse()
data = res.read()
trending_tech_articles = data.decode('utf-8')

#Converting JSON to pandas dataframe
parsed_data = json.loads(trending_tech_articles)
article_data = parsed_data["data"]
df = pd.DataFrame(article_data)
print(df)