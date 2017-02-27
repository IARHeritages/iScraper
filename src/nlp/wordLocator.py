'''
Created on Feb 27, 2017

@author: maltaweel
'''

from nltk.tokenize import word_tokenize

class Locator:
    
    def spans(self,txt):
        tokens=word_tokenize(txt)
        offset = 0
        for token in tokens:
            offset = txt.find(token, offset)
            yield token, offset, offset+len(token)
            offset += len(token)


s = "And now for something completely different and."
loc=Locator()
for token in loc.spans(s):
    print token
    assert token[0]==s[token[1]:token[2]]