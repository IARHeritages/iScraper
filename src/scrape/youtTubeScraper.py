'''
Created on Dec 7, 2016

Module to scrape data from a YouTube search

@author: maltaweel
'''

'''
This simply gets some data from a record within PAS.

The data recovered are the object, image, and description

Created on Jul 27, 2016

@author: maltaweel
'''
from bs4 import BeautifulSoup
import time
import urllib2


# The base url for the example
url = 'https://www.youtube.com/results?q=%22Roman+Empire%22+%2B+%22Britain%22&sp=EgQIBRAB'

#current time stamp to be used in naming the jpg file created
timestamp = time.asctime() 

# Parse HTML of article, aka making soup
soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")

# Scrape article main img
links = soup.find_all('h3')
for link in links:
    
    #get the current time
    timestamp = time.asctime() 
    lk=link.findAll("a")
    for l in lk:
        title=l['title']
        href="https://www.youtube.com/"+l['href']
        print(href)
   
links = soup.find_all('div') 
for link in links:
    
    #get the current time
    timestamp = time.asctime() 
    lk=link.findAll("a")
    for l in lk:
        print(l)
        