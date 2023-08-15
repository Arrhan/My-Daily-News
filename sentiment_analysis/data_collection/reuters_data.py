#Data extraction for analysis
keywords =['OpenAI']
#,'Google','Microsoft','Amazon','Facebook','Twitter','Biden','Trump','Modi','Apple']
#Sources
sources = ['Reuters','Reddit','Twitter | Techcrunch']

#Reuters
import requests
from bs4 import BeautifulSoup

for keyword in keywords:
    url = 'https://www.reuters.com/site-search/?query='+keyword+'&sort=relevance&offset=0&date=past_month'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link_elements = soup.find_all('a', {'data-testid': 'link'})
    for title in link_elements:
        print(title.get_text())



