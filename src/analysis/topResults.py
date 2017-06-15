'''
Created on Apr 21, 2017

@author: maltaweel
'''

from analysis import average_std
import operator
import os
import csv
import sys

class TopResults(average_std.Analysis):
    
    def loadData(self,pn,n):
    
        os.chdir(pn)
        
       
        rst={}
        i=0
        for filename in os.listdir(os.getcwd()):
            
            if(filename == ".DS_Store"):
                continue
           
            dct={}
            print(filename)
            with open(filename, 'rU') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
                
                ii=0
                try:
                    for row in reader:
                            
                        if(ii==0):
                            ii=ii+1
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
                
            ffinal={}
                
            for key, value in sorted(dct.iteritems(), key=lambda (k,v): (v,k),reverse=True):
                print(key+":"+str(value))
                    
                if(ii<n):
                    ffinal[key]=value
                ii+=1
                
            rst[str(i)]=ffinal
            i=i+1
        return rst
    
    def topResults(self,dct,n):
        
        top={}
    
        for i in range(0,100):
            ffinal={}
            for s in dct:
                v=dct[s]
                print(i)
                ffinal[s]=v[i]
            
            
   
                
            final={}
            ii=0
            for key, value in sorted(ffinal.iteritems(), key=lambda (k,v): (v,k),reverse=True):
                print(key+":"+str(value))
                if(ii<n):
                    final[key]=value
                    ii+=1
                else:
                    break
            top[str(i)]=final
        return top
            
    def printResults(self,get,type):
    
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/iScraper/output'
        
        filename=path+'/'+'top_results_'+type+'.csv'
        
        fieldnames = ['Number','Term','Value']
        
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()

            for ii in get:
                nn=int(ii)
                a=get[ii]
                
                for s in a:
                    writer.writerow({'Number':str(nn),'Term': str(s),'Value':str(a)})       

typ="lda"
t=TopResults()

# get the working path
os.chdir("../")
pn=os.path.abspath('../')
pn=pn+"/python_work"+"/iScraper/"+typ

res=t.loadData(pn,11)
t.printResults(res,typ)