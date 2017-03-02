'''
Created on Oct 12, 2016

@author: maltaweel
'''
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumScraper:


    def __init__(self,driverLocation,ls):
        self.driverLocation=driverLocation
        self.list=ls
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/output'
        
        filename=path+'/'+'output.csv'
        
        self.csvfile=filename
        
    def runScraper(self):
        browser=webdriver.Chrome(self.driverLocation)
        base_url=u'https://twitter.com/search?q='
        
        fieldnames = ['Number','Tweet']
        
        with open(self.csvfile, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            
            tt=0
            for i in self.list:
            
                query=unicode(i,"utf-8")
            
                print(query)
                url=base_url + query+" brexit&src=typd"


                browser.get(url)
                time.sleep(1)

                body=browser.find_element_by_tag_name('body')

                for _ in range(2000):
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.2)

                    tweets = browser.find_elements_by_class_name('tweet-text')

                    for tweet in tweets:
                        print(str(tt)+" : "+tweet.text)
                        writer.writerow({'Number': str(tt),'Tweet':tweet.text.encode("utf-8")})
                        tt=tt+1
ls=["Roman Empire"]                    
s=SeleniumScraper("/Users/maltaweel/Desktop/chromedriver",ls)
s.runScraper()