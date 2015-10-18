from django.db import models

class Place(models.Model):
	# sourceID=models.IntegerField()
	# source=models.TextField()	
	name=models.TextField()
	lat=models.TextField()	
	lng=models.TextField()	
	reward=models.TextField()
	offerPoints=models.TextField()
	offerText=models.TextField()
	description=models.TextField()
	questOrder=models.TextField()
	placeType=models.TextField()
	# rating=models.TextField()
	# placeID=models.IntegerField()	


