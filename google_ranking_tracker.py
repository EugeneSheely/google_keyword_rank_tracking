import requests
import re
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import random

def google_results(keyword, n_results):
    headers = {"User-Agent": "Mozilla/5.0"}
    cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}
    query = keyword
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    number_result = n_results
    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    response = requests.get(google_url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result if "url" in str(i)]
    links=[i.group(1) for i in results if i != None]
    return (links)


list_of_keywords = ["*YOUR KEYWORDS HERE*"]
list_of_website_domains = ["*YOUR WEBSITE AND COMPETITORS HERE"]


for i in list_of_keywords:
  list_of_results = google_results(i,21)
  results = []
  results.append(i)
  for x in list_of_website_domains:
    url = ""
    index = ""
    for y in list_of_results:
      if y.find(x) > -1:
        url = y
        index = list_of_results.index(y)+1
        results.append(url)
        results.append(index)
        #the break will give the first result which allows content to fit in csv, removing it will give multiple results.
        break
    if url == "":
      results.append("Not in top 20")
      results.append("Not in top 20")

  print(results)
  time.sleep(random.randint(5,10))
