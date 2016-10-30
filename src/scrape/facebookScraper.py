'''
Created on Oct 28, 2016

@author: maltaweel
'''
import facebook
from facebook import requests

def getSearch():
        token = 'EAACEdEose0cBAKgjwbzaAFtuTpsRaZAlg7XPNwdgC4swKlwgMsZAmCaxhL3YTkpBFfzDj87BFQa7E72e3hKcSWFIr3CDExkP93txZCZBCL75mAGsM83NMvUfJOQJEjrkdudA3cQcI3HuIr8zrGIyW2bOeTtptmYlHMtYwZCcjFgZDZD'

        graph = facebook.GraphAPI(token)
        profile = graph.get_object("me")
        print profile

        query="iron age"
        p=requests.get("https://graph.facebook.com/search?access_token=" + token +  "&q=" + query + "&type=page")
        li=[]
        for i in p:
            li.append(i)

        return li


li=getSearch()
   

