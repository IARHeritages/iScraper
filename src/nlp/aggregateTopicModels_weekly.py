'''
Created on Jun 16, 2017

@author: maltaweel
'''
import os
import csv
import sys
import numpy

class AggregateTopicModels:
    
    def readAndAddFiles(self):
        
        # get the current working path
        os.chdir("../")
        pn=os.path.abspath('../')
        os.chdir(pn+'/results')
        
        results={}
        n=0
        for filename in os.listdir(os.getcwd()):
            
            if(n==7):
                break;
            if(filename == ".DS_Store" in filename or ".csv" not in filename):
                continue
            
            with open(filename, 'rU') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                
                i=0
                try:
                    for row in reader:
                        if row in ['\n', '\r\n']:
                            continue
                        
                        if(i==0):
                            i=i+1
                            continue
                        
                        term=row[0]
                        value=float(row[1])
                    
                        if term in results:
                            
                            ls=results.get(term)
                            ls.append(value)
                        
                        else:
                            ls=[value]
                            dict2 ={term: ls }
                            results.update(dict2)
                     
                except csv.Error, e:
                    sys.exit('line %d: %s' % (reader.line_num, e))
            n+=1
    
        return results
    
    def doMaths(self,results,r):
        
        output={}
        
        ls=results.get(r)
            
            
        mean=numpy.mean(ls)
        std=numpy.std(ls, ddof=1)
        
        output['mean']=mean
        output['std']=std
        
        return output
    
    
    def printResults(self,dct,n):
        
        #     os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/output'
        
        filename=path+'/'+'aggregated_topic_model_results'+str(n)+'.csv'
        
        fieldnames = ['Term','Mean','STD']
        
        
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in dct:
                v=dct[key]
                mean=v['mean']
                std=v['std']
                writer.writerow({'Term': str(key.encode("utf-8")),'Mean':str(mean),'STD':str(std)})
                

atm=AggregateTopicModels()
results=atm.readAndAddFiles()

m={}
for r in results:
    v={}
    output=atm.doMaths(results, r)
    v['mean']=output['mean']
    v['std']=output['std']
    m[r]=v
    
atm.printResults(m,14)
    
    