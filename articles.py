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
trending_tech_topics='OR '
trending_business_topics='OR '

#Adding google trends to trending_topics
for i in range(0,15):
    trend_topics+=google_trends.trending_topics[0][i] + " OR "

#Adding tech_search keywords to trending_tech_topics
if len(google_trends.tech_searches)<15:
    for i in range(0,len(google_trends.tech_searches)):
        for j in range(0,len(google_trends.tech_searches['entityNames'][i])):
            trending_tech_topics+=google_trends.tech_searches['entityNames'][i][j] + " OR "
else:
    for i in range(0,15):
        for j in range(0,len(google_trends.tech_searches['entityNames'][i])):
            trending_tech_topics+=google_trends.tech_searches['entityNames'][i][j] + " OR "

#Adding business_search keywords to trending_business_topics
if len(google_trends.business_searches)<15:
    for i in range(0,len(google_trends.business_searches)):
        for j in range(0,len(google_trends.business_searches['entityNames'][i])):
            trending_business_topics+=google_trends.business_searches['entityNames'][i][j] + " OR "
else:
    for i in range(0,15):
        for j in range(0,len(google_trends.business_searches['entityNames'][i])):
            trending_business_topics+=google_trends.business_searches['entityNames'][i][j] + " OR "

#Final list of topics to sift for news articles REMOVE LAST OR FROM trending_topics
main_topics = economy+technology+business+politics+other
trending_topics=str(trend_topics)+'researchers'
trending_tech_topics=str(trending_tech_topics)+'scientists OR scientist'
trending_business_topics=trending_business_topics+'research'
print(trending_topics)
print(main_topics)

#ARTICLES ------
conn = http.client.HTTPConnection('api.mediastack.com')

params_tech = urllib.parse.urlencode({
    'access_key': '78bacb491fd29aad5689fd3809353ba9',
    'keywords': main_topics,
    'sources': 'cnn,nytimes',
    'sort':'popularity',
    'date': previous_date,
    'limit': 45
    })

conn.request('GET', '/v1/news?{}'.format(params_tech))

res = conn.getresponse()
data = res.read()
articles = data.decode('utf-8')

print("CNN and NYTimes articles:")
print(articles)