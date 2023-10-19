#This script is to simply extract top titles from AP news for a general overview of the news
import requests 
from bs4 import BeautifulSoup 

titles=[]
keywords =['OpenAI','Google','Microsoft','Amazon','Facebook','Twitter','Biden','Trump','Modi','Apple']

#Scraping AP news titles // MAKE INTO DICTIONARY FOR EACH KEYWORD AND STORE AS LIST
for keyword in keywords:
    url = f'https://apnews.com/search?q={keyword}#nt=navsearch'
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html5lib') 
    ap_titles=soup.find_all('span',class_='PagePromoContentIcons-text')
    for title in ap_titles[5:]:
        titles.append(title.string)
    print(titles)