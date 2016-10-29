'''
Created on Oct 28, 2016

@author: maltaweel
'''
import facebook
from facebook import requests

def getSearch():
        token = 'EAACEdEose0cBAJLrzut4iiCif3Ff3ZCGLGCIXuWYqTV5RC9ymAGc0GotTH71vsoLexaPXVHRzx9ZAnhZAiZBEgZCtGuBQrm3D0ryjFBupO24LNQlZBJ1B4BEEMgvOf1bZBjwyYMENjAZCXnapmKRK5J2OrPA4rINdfB64hZBeJlRVEgZDZD'

        graph = facebook.GraphAPI(token)
        profile = graph.get_object("me")
        print profile

        query="iron age"
        p=requests.get("https://graph.facebook.com/search?access_token=" + token +  "&q=" + query + "&type=page")
        list=[]
        for i in p:
            list.append(i)

        return list


list=getSearch()
print(list)    

