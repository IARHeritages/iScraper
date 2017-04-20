'''
Created on Mar 9, 2017

@author: maltaweel
'''
import os
import gensim
import csv
import re
import text
import sys
import codecs

class TextRemover:
    
    def retrieveText(self,pn,terms):
        result={}
        os.chdir(pn+'/output')
        
        with open('output_vote_remain_Dark_Age.csv', 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter='*', quotechar='|') 
            i=-1
            try:
                for row in reader:
                    
                    if(i==-1):
                        i=i+1
                        continue
                    if(len(row)<2):
                        continue
                    text=row[1]
                    
                    tFalse=True
                    for term in terms:
                        if (term in text) or (term.lower() in text.lower()): 
                            tFalse=False
                            break
                    
                    for s in result:
                        t=result[s]
                        if(text in t):
                            tFalse=False
                            break
                    if(tFalse==True ):
                        result[str(i)]=text
                    i=i+1
            except csv.Error, e:
                sys.exit('line %d: %s' % (reader.line_num, e))
                 
                 
            return result

    def printResults(self,result,nn):
        
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/iScraper/output'
        
        filename=path+'/'+'output_'+nn+'.csv'
        
        fieldnames = ['Number','Tweet']
        
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            writer.writeheader()
            
            for key in result:
                v=result[key]
                writer.writerow({'Number': str(key.encode("utf-8")),'Tweet':'*'+v})

os.chdir("../")
pn=os.path.abspath('../')
#terms=["'Holy' Roman","Holy#","Holy Roman","#Holy #Roman",]
terms=["dfdsfsdfdfssf"]
tr=TextRemover()
result=tr.retrieveText(pn,terms)
tr.printResults(result,"vote_remain_Dark_Age2")