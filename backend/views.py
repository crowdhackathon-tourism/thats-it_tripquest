import json, requests
from utils import *
from config import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.core.management import call_command
from sample import *

#default
location="37.9897402,23.680751"

@api_view()
def search(request,query,lat,lng):
    location =str(lat) +',' +str(lng)
    keyword=query
    url=googlePlacesURL + "nearbysearch/json?location=" + location + "&radius=5000&keyword=" + keyword + "&key=" + googlePlacesKey
    response=safeRequestJSON(url)
    data=fetchDetailsFromPlaces(response)
    return Response([model_to_dict(ob,exclude=['id']) for ob in data])

@api_view()
def simpleSearch(request,query):
    url=googlePlacesURL + "nearbysearch/json?location=" + location + "&radius=5000&keyword=" + query + "&key=" + googlePlacesKey
    response=safeRequestJSON(url)
    data=fetchDetailsFromPlaces(response)
    return Response([model_to_dict(ob,exclude=['id']) for ob in data])    

@api_view()
def searchRewarding(request,query):
    url=googlePlacesURL + "nearbysearch/json?location=" + location + "&radius=5000&keyword=" + query + "&key=" + googlePlacesKey
    response=safeRequestJSON(url)
    data=fillRewardingPlaces(response)
    return Response([model_to_dict(ob,exclude=['id','offerPoints','offerText','questOrder','description']) for ob in data])    

@api_view()
def searchConsuming(request,query):
    url=googlePlacesURL + "nearbysearch/json?location=" + location + "&radius=5000&keyword=" + query + "&key=" + googlePlacesKey
    response=safeRequestJSON(url)
    data=fillConsumingPlaces(response)
    return Response([model_to_dict(ob,exclude=['id','reward','questOrder','description']) for ob in data])   

@api_view()
def quest(request,questID):
    if questID=='1':
        data=mock1()
    elif questID=='2':
        data=mock2()
    elif questID=='3':
        data=mock3()    
    response={'results':[model_to_dict(ob,exclude=['id']) for ob in data],'name':'first quest','desc':'malakies','img':'http://lorempixel.com/400/200/transport'}
    return Response(response)  

@api_view()
def quests(request):
    data=mock1()
    response1={'results':[model_to_dict(ob,exclude=['id']) for ob in data],'name':'Historical Quest','desc':'The most historic places of Athens','img':'https://upload.wikimedia.org/wikipedia/commons/d/da/The_Parthenon_in_Athens.jpg'}
    data=mock2()
    response2={'results':[model_to_dict(ob,exclude=['id']) for ob in data],'name':'Classical Quest','desc':'A classic quest that everyone owes to complete during his visit in Athens','img':'http://www.thinkathens.com/wp-content/uploads/2015/02/Syntagma-square.jpg'}
    data=mock3()
    response3={'results':[model_to_dict(ob,exclude=['id']) for ob in data],'name':'Music Quest','desc':'A trip to the best music places of Athens','img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQETGu3hczrsitfVNPwisIXSRACXPz7bH-RvbUPuieUjO62njCMhw'}
    response=[response1,response2,response3]
    return Response(response)      

