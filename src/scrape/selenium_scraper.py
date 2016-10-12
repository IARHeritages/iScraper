'''
Created on Oct 12, 2016

@author: maltaweel
'''
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumScraper:

    def __init__(self,driverLocation,ls):
        self.driverLocation=driverLocation
        self.list=ls
        
    def runScraper(self):
        browser=webdriver.Chrome(self.driverLocation)
        base_url=u'https://twitter.com/search?q='
        
        for i in self.list:
            
            query=unicode(i[0],"utf-8")
            
            print(query)
            url=base_url + query


            browser.get(url)
            time.sleep(1)

            body=browser.find_element_by_tag_name('body')

            for _ in range(5):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.2)

                tweets = browser.find_elements_by_class_name('tweet-text')

                for tweet in tweets:
                    print(tweet.text)