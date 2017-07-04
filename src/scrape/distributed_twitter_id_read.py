'''
Created on Jun 22, 2017

@author: maltaweel
'''

import os   
import distributed_lda 
import distributed_hdp
import multiprocessing
    
CONSUMER_KEY = "Zy2qmilvNW5K7ceQ6NGAlffGT"
CONSUMER_SECRET = "9U8dcycd3FvGTbGWECfiGOkUelU0RPcWvV7XcSF5iys8zqu105"
OAUTH_TOKEN = "871743012602294272-LGiaEMDVelZ7Ru0GDDChfhaW84SITMk"
OAUTH_TOKEN_SECRET = "JZRci9fT7P26Ap5ubivG7MLv8pDsXR9i7d9eFXm7SSURt"
fle="brexit_tweets_ids"

def doTopicModel(analysis,filename):
            
    hdp.applyModel(analysis, 70) 
    hdp.printNewResults(70,"hdp",filename,output)
            
    lda.applyModel(analysis, 70)
    lda.printNewResults(70,"lda",filename,output)
    

def runThis():
    for filename in os.listdir(path):
    
        if ".DS_Store" not in filename:
        
    
            with open(path+filename, 'r') as filehandle:
                lines = filehandle.readlines()
        
                txt=""
                for line in lines:
                    line=line.split(",")
                    for l in line:
                        if '"text":' not in l:               
                            continue
                        else:
                            ll=l.split('":')
                            txt=txt+ll[1]+". "
            
                txt.replace("}","")
                txt.replace("]","")
            
                analysis.append(txt)
                pool.apply_async(doTopicModel, [analysis,filename])
                del analysis[:]
                print(filename)
           
os.chdir("../")
pn=os.path.abspath('../')
output=pn+'/results/'
path=pn+'/tweets/'
lda=distributed_lda.LDA()
hdp=distributed_hdp.HDP()
analysis=[]
pool = multiprocessing.Pool(2)
runThis()

