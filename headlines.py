import datetime
import pandas as pd
from newsapi import NewsApiClient

#Setting dates to get news articles from last 24 hours
current_date = datetime.datetime.today().strftime ('%Y-%m-%d')

previous_date = datetime.datetime.today() - datetime.timedelta(days=5)
previous_date=previous_date.strftime ('%Y-%m-%d')

#KEYWORDS ------
economy = 'inflation OR government OR stock market OR recession OR rally OR job market '
business = 'OR Venture Capital OR Investment OR startups OR Morgan OR BlackRock OR Meta OR Facebook OR NASA OR Tesla OR SpaceX OR Apple OR Microsoft OR Amazon OR Nvidia OR Google OR Twitter OR X '
technology = 'OR Bill Gates OR Zuckerberg OR Musk OR ChatGPT OR A.I. OR artifical intelligence OR machine learning OR software OR hardware OR DeepMind OR Chips OR Jeff Bezos  OR electric vehicles OR Larry Bird OR Brin OR chatbot OR OpenAI '
politics = 'OR Republicans OR GOP OR G.O.P. OR Biden OR Democrats OR Modi OR Jinpeng OR elections'
other = 'OR global warming OR heat OR university OR college admissions OR scientist OR Obama OR research OR researchers '
trending_topics = ''

other_topics = economy+other+politics+trending_topics

#API INITIALIZATION ------
newsapi = NewsApiClient(api_key='6de831c22296464bb0323ebb5b9a9bfd')

#HEADLINES ------
wsj_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')
tech_headlines = newsapi.get_top_headlines(country="us",
                                           category='technology',
                                           page_size= 10
                                           )
business_headlines = newsapi.get_top_headlines(country="us",
                                               category='business',
                                               page_size= 10
                                               )
other_headlines = newsapi.get_top_headlines(country="us",
                                            category='general',
                                            page_size= 10
                                               )

#print(wsj_headlines['articles'])
#print(tech_headlines['articles'])
#print(business_headlines['articles'])
#print(other_headlines['articles'])

#WSJ articles ------ *******

#SAVING ARTICLES TO A DATABASE (CSV FORMAT AND SAVE TO COMPUTER FOR NOW) - LATER USED TO ADD TO WEBSITE ------