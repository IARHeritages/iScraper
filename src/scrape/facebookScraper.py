'''
Created on Oct 28, 2016

@author: maltaweel
'''
import facebook


token = 'EAACEdEose0cBAJLrzut4iiCif3Ff3ZCGLGCIXuWYqTV5RC9ymAGc0GotTH71vsoLexaPXVHRzx9ZAnhZAiZBEgZCtGuBQrm3D0ryjFBupO24LNQlZBJ1B4BEEMgvOf1bZBjwyYMENjAZCXnapmKRK5J2OrPA4rINdfB64hZBeJlRVEgZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print profile

        

