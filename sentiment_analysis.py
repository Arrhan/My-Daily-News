# import the required packages and libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# set up a new Selenium driver
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# define the username of the profile to scrape and generate its URL
username = "bright_data"
URL = "https://twitter.com/" + username + "?lang=en"

# load the URL in the Selenium driver
driver.get(URL)

# wait for the webpage to be loaded
# PS: this considers a profile page to be loaded when at least one tweet has been loaded
#     it might not work well for restricted profiles or public profiles with zero tweets
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
except WebDriverException:
    print("Tweets did not appear! Proceeding after timeout")

# extract the information using either CSS selectors (and data-testid) or XPath
name = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserName"]').text.split('\n')[0]
bio = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserDescription"]').text
location = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserLocation"]').text
website = driver.find_element(By.CSS_SELECTOR,'a[data-testid="UserUrl"]').text
join_date = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserJoinDate"]').text
following_count = driver.find_element(By.XPATH, "//span[contains(text(), 'Following')]/ancestor::a/span").text
followers_count = driver.find_element(By.XPATH, "//span[contains(text(), 'Followers')]/ancestor::a/span").text
tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

# print the collected information
print("Name\t\t: " + name)
print("Bio\t\t: " + bio)
print("Location\t: " + location)
print("Website\t\t: " + website)
print("Joined on\t: " + join_date)
print("Following count\t: " + following_count)
print("Followers count\t: " + followers_count)

# print each collected tweet's text
for tweet in tweets:
    tweet_text = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text
    print("Tweet text\t: " + tweet_text)