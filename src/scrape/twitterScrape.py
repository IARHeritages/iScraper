'''
Created on Oct 12, 2016

@author: maltaweel
'''

import requests
from bs4 import BeautifulSoup
from poultry import readline_dir
import os 
import io
import csv
from poultry.utils import get_file_names

pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
        

#The data file path is now created where the data folder and dataFile.csv is referenced
path=os.path.join(pn,'tweets')

texts=[]
ids=[]
screen_names=[]
dates=[]

for tweet in readline_dir(path):
    ca=tweet.created_at
    sn=tweet.screen_name
    idd=tweet.id
    text=tweet.text
    text.lower()
    
    if ('roman empire' in text or 'romanempire' in text):
        texts.append(text)
        ids.append(idd)
        screen_names.append(sn)
        dates.append(ca)
        
        
    
  
filename=pn+'/'+'roman_empire_results.csv'
        
fieldnames = ['ID','Date','Screen Name','Text']
        
with open(filename, 'wb') as csvf:
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)

    writer.writeheader()

    for s in texts:  
        ind=texts.index(s)
        
        ca=dates[ind]
        sn=screen_names[ind]
        date=dates[ind]
        idd=ids[ind]
        
        writer.writerow(
                        {'ID': str(idd).encode('utf-8'),'Date':str(date).encode('utf-8'),'Screen Name':sn.encode('utf-8'),'Text':s.encode('utf-8').strip()})
        
        
       
            
             
# print(fle.id, fle.parsed['user']['screen_name'])

#url=u'https://twitter.com/search?q='
#query=u'%ironage'

#r=requests.get(url+query)
#soup=BeautifulSoup(r.text,'html.parser')

#tweets = [p.text for p in soup.findAll('p',class_='tweet-text')]

#i=0
#for t in tweets:
#    if t 
#    i=i+1

