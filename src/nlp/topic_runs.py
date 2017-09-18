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
for i in range(10,100,10):
    for j in range(10,40,10):
        hdp=HDP() 
        results=hdp.retrieveText(pn)
        hdp.applyModel(results, i,j)
        hdp.printResults(i,j)    
    
#iterate and try a range of numbers for the number of topics
for i in range(10,100,10):
    for j in range(10,40,10):
        for k in range(20,50,10):
            lda=LDA()
            results=lda.retrieveText(pn)
            lda.applyModel(results, i,j,k)
            lda.printResults(i,j,k)