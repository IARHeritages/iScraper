'''
This module runs the topic models.

Created on Apr 20, 2017

@author: maltaweel
'''

from nlp.lda import LDA
from nlp.hdp import HDP

import os

# get the current working path
os.chdir("../")
pn=os.path.abspath('../')

hdp=HDP()   
lda=LDA()
 
#iterate and try a range of numbers for the number of topics
for nn in range(50,70,10):
    results=hdp.retrieveText(pn)
    hdp.applyModel(results, nn)
    hdp.printResults(nn)    
    
#iterate and try a range of numbers for the number of topics
for nn in range(50,70,10):
   
    results=lda.retrieveText(pn)
    lda.applyModel(results, nn)
    lda.printResults(nn)