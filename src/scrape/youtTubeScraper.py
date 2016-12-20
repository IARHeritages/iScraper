'''
Created on Dec 7, 2016

Module to scrape data from a YouTube search

@author: maltaweel
'''

from bs4 import BeautifulSoup
import time
import urllib2
import csv

titlez=[]
linkz=[]



# The base url for the example


#current time stamp to be used in naming the jpg file created
timestamp = time.asctime() 

# Parse HTML of article, aka making soup

nb=1

def generalLinks(url):
    # Scrape article main img
    soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
    links=soup.findAll(attrs={'class':'yt-uix-tile-link'})
    for link in links:
        print link['title']
        titlez.append(link['title'])
        print 'https://www.youtube.com/'+link['href']
        linkz.append('https://www.youtube.com/'+link['href'])
    findLinks(url)

def findLinks(url):
    soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
    lks=soup.findAll(attrs={'class':'yt-uix-button vve-check yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default'})
    
    for link in lks:
        a=link['aria-label'].split(" ")
        n=int(a[3])
        global nb
        if n>nb:
            nb=n
            generalLinks('https://www.youtube.com/'+link['href'])
            break
        
def printResults():
    with open('YouTubeLinks.csv', 'w') as csvfile:
        fieldnames = ['Title', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(titlez)):
            writer.writerow({'Title': titlez[i].encode('utf-8').strip(), 'Link': linkz[i].encode('utf-8').strip()})

url = 'https://www.youtube.com/results?q=%22Roman+Empire%22+%2B+%22Britain%22&sp=EgQIBRAB'   
findLinks(url)
printResults()    