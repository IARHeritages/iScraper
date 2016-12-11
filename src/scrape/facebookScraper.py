'''
Created on Oct 28, 2016

@author: maltaweel
'''
import facebook
from facebook import requests

def getSearch():
        token = 'EAACEdEose0cBALhsD3tTU4tORZAFY48AQio1wuY8X4t0yFxjGXkXpeYB5Wyb6DJl5Kj8jNISmeokG26OGuIsSk0hdZApaBdZCNqQsq0wv4lQgEEPkrA1g2CUbrn4PKozIoJmsZBDvvM5dDHcxsVV0DP9mcikG34ZCaXpJSrlMOQZDZD'

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
   

