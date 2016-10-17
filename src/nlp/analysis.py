'''
Created on Oct 17, 2016

@author: maltaweel
'''

import nltk
from nltk.corpus import treebank

sentence = """At eight o'clock on Thursday morning... 
Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()