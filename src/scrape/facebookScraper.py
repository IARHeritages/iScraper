'''
Created on Oct 28, 2016

@author: maltaweel
'''
import facebook
from facebook import requests

def getSearch():
        token = 'EAACEdEose0cBAMnTy6MY4QAIAzPczvNZCUcdECAIncgmZCXsopgBMwLUJeAosEWQS4cN8yBeHuIiM4aicRQqooDLrrQEYBRijm3ph8PLk1z6flA2qUmLhxykOq68EdHcBX3GoxPgHGQOWS4ZCMk5GnM6WbXfifL6wGNYMkjbgZDZD'

        graph = facebook.GraphAPI(token)
        profile = graph.get_object("me")
        print profile

        query="iron age"
        stringRequest="https://graph.facebook.com/search?access_token=" + token +  "&q=" + query + "&type=page"
        p=requests.get(stringRequest)
        li=[]
        for i in p:
            li.append(i)

        return li


li=getSearch()
   

