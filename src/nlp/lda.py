'''
The class applies a Latent Dirichlet Allocation analysis and outputs the results.

Created on Mar 2, 2017

@author: maltaweel
'''
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import os
import gensim
import csv
import re


class LDA:
    
    listResults=[]
    
    '''
    Method to get the text output from the scraping.
    '''
    def retrieveText(self):
        
        os.chdir("../")
        pn=os.path.abspath('../')
        os.chdir(pn+'/output')
        with open('output.csv', 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter='*', quotechar='|')
            
            i=0
            for row in reader:
                if(i==0):
                    i=i+1
                    continue
                if(len(row)<2):
                    continue
                text=row[1]
                text=re.sub('"','',text)
                text=re.sub(',','',text)
                doc_set=[text.decode('ISO-8859-1').strip()]
                self.applyModel(doc_set)
    
    '''The Latent Dirichlet Allocation model applied to the text'''
    def applyModel(self, doc_set):
        
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
    
            # convert tokenized documents into a document-term matrix
            corpus = [dictionary.doc2bow(text) for text in texts]

            # generate LDA model
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
            t=ldamodel.print_topics(num_topics=2, num_words=10)
            
            #term and values from text
            result_dict=self.addTotalTermResults(t)
            
            #add results to total kept in a list     
            self.addToResults(result_dict)
    
    '''The terms and values from text.
    @return the  term and values'''
    def addTotalTermResults(self,t):
        result_dict={}
        for a,b in t:
                text=re.sub('"',"",b)
                text.replace(" ","")
                txts=text.split("+")
                for t in txts:
                    ttnts=t.split("*")
                    v=float(ttnts[0])
                    t=ttnts[1]
                    if(t in result_dict):
                        continue
                    else:
                        t=t.strip()
                        result_dict[t]=v 
                           
        return result_dict
                        
    '''Add dictionary to a list of results from each text'''        
    def addToResults(self,result_dict):
            self.listResults.append(result_dict)
    
    '''Output results of the analysis'''    
    def printResults(self):
        
        os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/iScraper/output'
        
        filename=path+'/'+'lda_results.csv'
        
        fieldnames = ['Term','Value']
        
        dct=self.dictionaryResults()
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in dct:
                v=dct[key]
                writer.writerow({'Term': str(key.encode("utf-8")),'Value':str(v)})
        

    '''Method aggregates all the dictionaries for keyterms and theri values.
     @return dct a dictionary of all keyterms and values'''
                
    def dictionaryResults(self):
        #set the dictionary
        dct={}
        
        #iterate over all tweets and add to total dictionary
        for dictionary in self.listResults:
                for key in dictionary:
                    
                    v=dictionary[key]
                    if(key in dct):
                        vv=dct[key]
                        vv=v+vv
                        dct[key]=vv
                    else:
                        dct[key]=v 
                        
        return dct

lda=LDA()
lda.retrieveText()
lda.printResults()