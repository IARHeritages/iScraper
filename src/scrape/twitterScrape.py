'''
Created on Oct 12, 2016

@author: maltaweel
'''

import requests
from bs4 import BeautifulSoup
from poultry import readline_dir

for tweet in readline_dir('./tweets/'):
     print(tweet.id, tweet.parsed['user']['screen_name'])

url=u'https://twitter.com/search?q='
query=u'%ironage'

r=requests.get(url+query)
soup=BeautifulSoup(r.text,'html.parser')

tweets = [p.text for p in soup.findAll('p',class_='tweet-text')]

i=0
for t in tweets:
    print(str(i)+": "+t)
    i=i+1

