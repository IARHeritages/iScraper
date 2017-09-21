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
import sys

csv.field_size_limit(sys.maxsize)
class LDA:
    ldamodel=None
    dictionary=None
    corpus=None
    
    listResults=[]
    
    '''
    Method to get the text output from the scraping.
    @param pn the path to find the relevant text
    '''
    def retrieveText(self,pn):
        del self.listResults[:]
        
        doc_set=[]
        os.chdir(pn+'/output')
        en_stop = get_stop_words('en')
        result=[]
        for filename in os.listdir(os.getcwd()):
            txt=''
            if(filename == ".DS_Store" or "lda" in filename or "hdp" in filename or ".csv" not in filename):
                continue
            print(filename)
            with open(filename, 'rU') as csvfile:
                reader = csv.reader(csvfile, quotechar='|') 
                
                i=0
                try:
                    for row in reader:
                        if row in ['\n', '\r\n']:
                            continue;
                        if(i==0):
                            i=i+1
                            continue
                        if(len(row)<1):
                            continue
                        
        #                if i==100:
        #                    break
                        text=''
                        for r in row:
                            text+=r.strip()
                            
                        text=re.sub('"','',text)
                        text=re.sub(',','',text)
                        text.strip()
                        tFalse=True
                        
                        if(len(result)==0):
                            result.append(text)
                            i+=1
                            txt=txt+" "+text
     #                       continue
     #                   for s in result:
     #                       if(text in s):
     #                           tFalse=False
     #                           break
                            
                        if(tFalse==True):
     #                       result.append(text)
                             txt=txt+" "+text
                             
                             if text==' ':
                                 continue
                             
                             tokenizer = RegexpTokenizer(r'\w+')
                             text = tokenizer.tokenize(unicode(text, errors='replace'))
                             stopped_tokens = [t for t in text if not t in en_stop]
                             
                             doc_set.append(stopped_tokens)  
                        i+=1 
                except csv.Error, e:
                    sys.exit('line %d: %s' % (reader.line_num, e))
            
               
     #           doc_set.append(unicode(txt, errors='replace'))
            
        return doc_set

    '''The Latent Dirichlet Allocation model applied to the text
     @param doc_set the text
     @param nn the topic number
     @param wn the word number
     @param p the number of passes'''
     
    def applyModel(self, doc_set, nn,wn,p):
        
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
        
            print(i)
            
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
            corpus = [dictionary.doc2bow(text,allow_update=True) for text in texts]
            
            if(self.dictionary==None):
                self.dictionary=dictionary
                self.corpus=corpus
            
            if len(dictionary)<1:
                continue
            
            # generate LDA model
            ldamodel= gensim.models.ldamodel.LdaModel(corpus, num_topics=nn, update_every=1,id2word = dictionary, passes=p)
#            ldamodel=None
#            if(self.ldamodel==None):
#                self.ldamodel= gensim.models.ldamodel.LdaModel(corpus, num_topics=nn, update_every=1,id2word = dictionary, passes=20)
#                ldamodel = self.ldamodel
            
#            else:
#                self.dictionary.merge_with(dictionary)
#                ldamodel=models.ldamodel.LdaModel.load("lda_results")
#                self.ldamodel= models.ldamodel.LdaModel(self.corpus, num_topics=nn, id2word = self.dictionary, passes=20)
#                self.ldamodel.update(corpus)
#                ldamodel=self.ldamodel        
                 
            t=ldamodel.print_topics(num_topics=nn, num_words=wn)
            
            
            #term and values from text
            result_dict=self.addTotalTermResults(t)
            
            #add results to total kept in a list     
            self.addToResults(result_dict)
            
  #          ldamodel.save("lda_results")
            
    
    '''The terms and values from text.
    @return result_dict dictionary of the term and values'''
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
                    t=str(a)+":"+t
                    if(t in result_dict):
                        continue
                    else:
                        t=t.strip()
                        result_dict[t]=v 
                           
        return result_dict
                        
    '''Add dictionary to a list of results from each text
    @param result_dict this is the resulting terms'''        
    def addToResults(self,result_dict):
            self.listResults.append(result_dict)
    
    '''Output results of the analysis
    @param nn the number of topics used for the output name
    @param i topic number
    @param j the word number
    @param p the pass number'''    
    def printResults(self,i,j,p):
        
  #     os.chdir('../')
        pn=os.path.abspath('../')
        path=pn+'/lda'
        
        filename=path+'/'+'lda_results'+"-"+str(i)+'-'+str(j)+'-'+str(p)+'.csv'
        
        fieldnames = ['Topic','Term','Value']
        
        dct=self.dictionaryResults()
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in dct:
                v=dct[key]
                tn=key.split(":")[0]
                kt=key.split(":")[1]
                writer.writerow({'Topic':str(tn),'Term': str(kt.encode("utf-8")),'Value':str(v)})
        
    '''Method aggregates all the dictionaries for keyterms and their values.
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
    
    def printNewResults(self, nn,typ,i,path):
                
        filename=path+'/'+typ+"_results"+str(nn)+"-"+str(i)+'.csv'
        
        fieldnames = ['Term','Value']
        
        dct=self.dictionaryResults()
        with open(filename, 'wb') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)

            writer.writeheader()
            
            for key in dct:
                v=dct[key]
                writer.writerow({'Term': str(key.encode("utf-8")),'Value':str(v)})