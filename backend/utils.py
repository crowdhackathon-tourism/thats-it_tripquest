from django.core.cache import cache
import json, requests
from django.db import models
from models import Place
from config import *


from django.core.cache import cache
import random


def safeRequestJSON(url):
	response=None
	cached=cache.get(url)
	if cached:
		response=cached
	else:
		try:
			response = requests.get(url=url).json()
			cache.set(url,response)
		except:
			pass	
	return response		


def fetchDetailsFromPlaces(response):
	places=[]
	for i in response['results']:
		place=Place()
		place.name = i['name']
		place.lat = str(i['geometry']['location']['lat'])
		place.lng = str(i['geometry']['location']['lng'])
		place.reward = ''
		pointsToSpend=random.randint(0,100)
		place.offerPoints=str(pointsToSpend)
		place.offerText= 'Get our special offer for ' +place.offerPoints + ' points'
		places.append(place)
	return places	

def fillRewardingPlaces(response):
	places=[]
	for i in response['results']:
		place=Place()
		ID=i['place_id']
		place=getDetailsForID(ID,place)
		place.reward = random.randint(0,100)
		pointsToSpend=''
		place.offerPoints=str(pointsToSpend)
		place.offerText= ''
		place.placeType='rewarding'
		places.append(place)
	return places

def fillConsumingPlaces(response):
	places=[]
	for i in response['results']:
		place=Place()
		ID=i['place_id']
		place=getDetailsForID(ID,place)
		place.reward = ''
		pointsToSpend=random.randint(0,100)
		place.offerPoints=str(pointsToSpend)
		place.offerText= 'Get our special offer for ' +place.offerPoints + ' points'
		place.placeType='consuming'
		places.append(place)
	return places				


def getDetailsForID(ID,place):
	url = googlePlacesURL + 'details/json?placeid=' + ID + '&key=' + googlePlacesKey
	print url
	data=safeRequestJSON(url)['result']
	place.name = data['name']
	place.lat = str(data['geometry']['location']['lat'])
	place.lng = str(data['geometry']['location']['lng'])
	return place


