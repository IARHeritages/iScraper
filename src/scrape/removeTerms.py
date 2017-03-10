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

class TextRemover:
    
    def retrieveText(self,pn,term):
        result={}
        os.chdir(pn+'/output')
        with open('output_roman_empire.csv', 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter='*', quotechar='|') 
            i=0
            try:
                for row in reader:
                    
                    if(i==0):
                        continue
                    if(len(row)<2):
                        continue
                    text=row[1]
                    
                    if (term.upper() in text) or (term.lower() in text): 
                        continue
                    else:
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
term="Holy Roman Empire"
tr=TextRemover()
result=tr.retrieveText(pn,term)
tr.printResults(result,"roman_empire2")