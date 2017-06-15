'''
Created on Jun 5, 2017

@author: maltaweel
'''

import os   
from nlp.lda import LDA
from nlp.hdp import HDP
    
    
CONSUMER_KEY = "Zy2qmilvNW5K7ceQ6NGAlffGT"
CONSUMER_SECRET = "9U8dcycd3FvGTbGWECfiGOkUelU0RPcWvV7XcSF5iys8zqu105"
OAUTH_TOKEN = "871743012602294272-LGiaEMDVelZ7Ru0GDDChfhaW84SITMk"
OAUTH_TOKEN_SECRET = "JZRci9fT7P26Ap5ubivG7MLv8pDsXR9i7d9eFXm7SSURt"
fle="brexit_tweets_ids"

os.chdir("../")
pn=os.path.abspath('../')
output=pn+'/results/'
path=pn+'/tweets/'
lda=LDA()
hdp=HDP()
analysis=[]

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
            
            
            hdp.applyModel(analysis, 70) 
            hdp.printNewResults(70,"hdp",filename,output)
            
            lda.applyModel(analysis, 70)
            lda.printNewResults(70,"lda",filename,output)
            del analysis[:]
            print(filename)


####           
#os.chdir('../')
#fileLocation=os.path.abspath('../')
#path=fileLocation+'/results/'+fle

#first, open the file and put into object f
#f = open(path, 'rU')
#rows=[]

#We can use a try clause to read the file
#try:
#    reader = csv.reader(f)
#    i=0
    
    #for loop
#    for row in reader:
#        print(row[0])
#        tweet = twitter.show_status(id=row[0])
#        text=tweet['text']
#        print(text)  
        
               
#then close the file
# finally:
#    f.close()
