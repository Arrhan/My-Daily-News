from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

#Trending topics
trending_topics = pytrends.trending_searches(pn='united_states')

#Realtime search trends on Google (Category = business)
#business_searches = pytrends.realtime_trending_searches(pn='US',cat='b',count=10)
#Business section does not yield too many useful results so will not use

#Realtime search trends on Google (Category = health)
tech_searches = pytrends.realtime_trending_searches(pn='US',cat='t')