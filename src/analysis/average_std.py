'''
Class for performing basic statistical analysis on terms and topic model results, 
such as mean and standard deviation for dictionary results (key term and value).

Created on Apr 21, 2017

@author: maltaweel
'''

import os
import csv
import sys
import numpy

class Analysis:
    
    '''
    Method to load files and organize terms with their topic model values.
    
    @param pn the path to use for data
    '''
    def loadData(self,pn):
    
        os.chdir(pn)
        
        dct={}
        
        for filename in os.listdir(os.getcwd()):
            
            if(filename == ".DS_Store"):
                continue
           
            print(filename)
            with open(filename, 'rU') as csvfile:
                reader = csv.reader(csvfile, delimiter='*', quotechar='|') 
                
                if(filename == ".DS_Store"):
                    continue
            
                with open(filename, 'rU') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
                    
                    i=0
                    try:
                        for row in reader:
                            
                            if(i==0):
                                i=i+1
                                continue
                            if(len(row)<2):
                                continue
                        
                            text1=row[0]
                            text2=row[1]
                           
                            v2=float(text2)
                            
                            if text1 in dct:
                                v=dct[text1]
                                v.append(v2)
                                dct[text1]=v
                            else:
                                v=[]
                                v.append(v2)
                                dct[text1]=v
                             
                    except csv.Error, e:
                        sys.exit('line %d: %s' % (reader.line_num, e))
                        
        return dct
    
    '''
    The mean calculation.
    
    @param dct the dictionary with values
    '''
    def mean(self,dct):
        rslt={}
        for s in dct:
            v=dct[s]
            a=numpy.average(v)
            rslt[s]=a
            
        return rslt
    
    '''
    The standard deviation calculation.
    
    @param dct the dictionary with values
    '''
    def standard_dev(self,dct):
        rslt={}
        for s in dct:
            v=dct[s]
            std=numpy.std(v)
            rslt[s]=std
            
        return rslt
            
    '''
    Method to print relevant term, average, and standard deviation results
    
    @param rslt1 this is the dictionary of mean values
    @param rslt2 this is the dictionary of standard deviation values
    '''    
    def printResults(self,rslt1,rslt2,typ):
    
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/iScraper/output'
        
        filename=path+'/'+'average_std_results_'+typ+'.csv'
        
        fieldnames = ['Term','Average','STD']
        
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()

            for s in rslt1:
                a=rslt1[s]
                std=rslt2[s]
                writer.writerow({'Term': str(s),'Average':str(a),'STD':str(std)})

tpe="lda"       
# get the working path
os.chdir("../")
pn=os.path.abspath('../')
pn=pn+"/"+tpe

#run the analysis
a=Analysis()
res=a.loadData(pn)
mean=a.mean(res)
std=a.standard_dev(res)
a.printResults(mean, std,tpe)

 
          
        