'''
Created on Jun 21, 2017

@author: maltaweel
'''
import os
import csv
import sys

class TermOverTime():
    
    
    def readAndFindTerm(self,terms):
        
        # get the current working path
        os.chdir("../")
        pn=os.path.abspath('../')
        os.chdir(pn+'/results')
        
        results={}
        
        
        for t in terms:
            lower=t.lower()
            
            for filename in os.listdir(os.getcwd()):
                
                time=filename.split("-")[1]
                time=time.split(".")[0]
                
                    
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
                            
                            if lower == term.lower():
                                
                                value=float(row[1])
                                v=str(term)+":"+str(value)
                                if time in results:
                            
                                    ls=results.get(time)        
                                    ls.append(v)
                        
                                else:
                                    ls=[v]
                                    dict2 ={time: ls }
                                    results.update(dict2)
                            
                            else:
                                continue
                     
                    except csv.Error, e:
                        sys.exit('line %d: %s' % (reader.line_num, e))
        return results
        
    def printResults(self,results):
        
        #     os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/results'
        
        filename=path+'/'+'term_over_time.csv'
        
        fieldnames = ['Time','Term','Value']
        
        
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in results:
                value=results[key]
                v=value.split(":")
                writer.writerow({'Time': str(key.encode("utf-8")),'Term':str(v[0]),'Value':str(v[1])})
                
                
t=TermOverTime()
terms=['brexit','iron age','roman empire']
results=t.readAndFindTerm(terms)
t.printResults(results)