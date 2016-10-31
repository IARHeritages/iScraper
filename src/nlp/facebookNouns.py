'''
Parser and NLTK for nouns in Facebook.

Created on Oct 28, 2016

@author: maltaweel
'''

from scrape import facebookScraper
import operator
import csv
import RAKE
import os
import nltk


class NLTK_Nouns():
    
    def __init__(self,text):
        self.text=text
        os.chdir('../')
        pn=os.path.abspath('../')


        path=os.path.join(pn,'input','keywords.txt')
        self.rake_object = RAKE.Rake(path)
    
    def getNouns(self):
        
        self.kList=[]
        for i in self.text:
            keywords = self.rake_object.run(i)
            
            for k in keywords:
                self.kList.append(k)
            
            
    
    def output(self):
        pn=os.path.abspath('../')
        path=os.path.join(pn,'input','output.csv')
        with  open(path, "wb") as ofile:
            writer = csv.writer(ofile, delimiter=',')
            writer.writerow(["Keyword","Count"])
            lines=[]
            for k in self.kList:
                w=k[0]
                v=k[1]
                line=[w,v]
                lines.append(line)
            writer.writerows(lines)
        
        
        ofile.close()
        
              


li=facebookScraper.getSearch()
print(li)

nltkN=NLTK_Nouns(li)
nltkN.getNouns()
nltkN.output()