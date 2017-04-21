'''
Created on Apr 20, 2017

@author: maltaweel
'''

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nlp import lda

import os
import gensim
import csv
import re
import text
import sys



class HDP(lda.LDA):
    hdp=None
    
    def applyModel(self, doc_set, nn):
        
        # reg. expression tokenizer
        tokenizer = RegexpTokenizer(r'\w+')

        # create English stop words list
        en_stop = get_stop_words('en')

        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()
    

        # list for tokenized documents in loop
        texts = []

        # loop through document list
        for i in doc_set:
    
            # clean and tokenize document string
            raw = i.lower()
            tokens = tokenizer.tokenize(raw)

            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in en_stop]
    
            # stem tokens
            #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
            # add tokens to list
            #texts.append(stemmed_tokens)
            texts.append(stopped_tokens)
            
            # turn our tokenized documents into a id <-> term dictionary
            dictionary = corpora.Dictionary(texts)
            
            if(self.dictionary==None):
                self.dictionary=dictionary
            
            # convert tokenized documents into a document-term matrix
            corpus = [dictionary.doc2bow(text,allow_update=True) for text in texts]
            
            if len(dictionary)<1:
                continue
            
            hdp=models.HdpModel(corpus, id2word=dictionary)
#          hdp=None
#          if(self.hdp==None):
#              self.hdp=models.HdpModel(corpus, id2word=dictionary)
#              hdp = self.hdp
            
#         else:
#             self.dictionary.merge_with(dictionary)
#              hdp=models.HdpModel.load("hdp_results")
#              self.hdp=models.HdpModel(hdp.corpus, id2word=self.dictionary)
#              self.hdp.update(corpus)
#              hdp=self.hdp
            
            
            t=hdp.print_topics(num_topics=-1, num_words=nn)
            
            #term and values from text
            result_dict=self.addTotalTermResults(t)
            
            #add results to total kept in a list     
            self.addToResults(result_dict)
            
#          hdp.save("hdp_results")
            
            
    def printResults(self,nn,i):
        
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/iScraper/results'
        
        filename=path+'/'+'hdp_results'+str(nn)+"-"+str(i)+'.csv'
        
        fieldnames = ['Term','Value']
        
        dct=self.dictionaryResults()
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in dct:
                v=dct[key]
                writer.writerow({'Term': str(key.encode("utf-8")),'Value':str(v)})

