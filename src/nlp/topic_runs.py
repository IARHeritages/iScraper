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
 
#iterate and try a range of numbers for the number of topics

for i in range(1,100):
    hdp=HDP()   
    results=hdp.retrieveText(pn)
    hdp.applyModel(results, 70)
    hdp.printResults(70,i)    
    
#iterate and try a range of numbers for the number of topics
for i in range(1,100):
    lda=LDA()
    results=lda.retrieveText(pn)
    lda.applyModel(results, 70)
    lda.printResults(70,i)