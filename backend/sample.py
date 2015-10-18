from utils import *

def mock1():
	places=[]

	place=Place()
	place=getDetailsForID('ChIJYe45yhm9oRQRGKJ4uHmgPxs',place)
	place.reward = str(40)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='The Parthenon is a former temple on the Athenian Acropolis, Greece, dedicated to the goddess Athena, whom the people of Athens considered their patron. Construction began in 447 BC when the Athenian Empire was at the peak of its power.'
	place.questOrder=str(1)
	place.placeType="rewarding"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJvQ93rRe9oRQRrRKw2L6lBR4',place)
	place.reward = str(40)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='The Ancient Agora of Classical Athens is the best-known example of an ancient Greek agora, located to the northwest of the Acropolis and bounded on the south by the hill of the Areopagus and on the west by the hill known as the Agoraios Kolonos, also called Market Hill.'
	place.questOrder=str(2)
	place.placeType="rewarding"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJKWScmxa9oRQRVULpHyK7GVU',place)
	place.reward = str(20)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='The Temple of Olympian Zeus, also known as the Olympieion or Columns of the Olympian Zeus, is a colossal ruined temple in the center of the Greek capital Athens that was dedicated to Zeus, king of the Olympian gods.'
	place.questOrder=str(3)
	place.placeType="rewarding"
	places.append(place)
	
	place=Place()
	place=getDetailsForID('ChIJb08llzu9oRQR6ZDRfxnRT40',place)
	place.reward = str(50)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='The National Historical Museum, founded in 1882, is the oldest of its kind in Greece. It is located in the Old Parliament House at Stadiou Street in Athens, which housed the Hellenic Parliament between 1875 and 1932.'
	place.questOrder=str(4)
	place.placeType="rewarding"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJdU4xH3ujoRQRzfcLEi50GnE',place)
	place.reward = ''
	pointsToSpend='35'
	place.offerPoints=str(pointsToSpend)
	place.offerText= 'Free bottle of Greek wine of your choice with ' + pointsToSpend + ' points'
	place.name='One of the top choices for Greek gourmet cuisine'
	place.description='Restaurant with traditional foods'
	place.questOrder=str(1)
	place.placeType="consuming"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJk4XyViK9oRQRz5_VHhupvS8',place)
	place.reward = ''
	pointsToSpend='20'
	place.offerPoints=str(pointsToSpend)
	place.offerText= 'Free coffee with' + pointsToSpend + ' points'
	place.description='An artistic place to drink coffee'
	place.questOrder=str(2)
	place.placeType="consuming"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJ9-naYEC9oRQRNHzbRl4WSbk',place)
	place.reward = ''
	pointsToSpend='40'
	place.offerPoints=str(pointsToSpend)
	place.offerText= 'Free coffee with' + pointsToSpend + ' points'
	place.description='One of the best hotels of Athens Center'
	place.questOrder=str(4)
	place.placeType="consuming"
	places.append(place)


	return places	

def mock2():
	places=[]

	place=Place()
	place=getDetailsForID('ChIJKWScmxa9oRQRVULpHyK7GVU',place)
	place.reward = str(40)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='Monument of Zeus'
	place.questOrder=str(1)
	place.placeType="rewarding"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJBznR1CK9oRQRgvc6KPVdI-c',place)
	place.reward = ''
	pointsToSpend='8'
	place.offerPoints=str(pointsToSpend)
	place.offerText= 'Free cake with your coffee , consuming ' + pointsToSpend + ' points'
	place.description='Cafe place'
	place.questOrder=str(2)
	place.placeType="consuming"
	places.append(place)

	return places	

def mock3():
	places=[]

	place=Place()
	place=getDetailsForID('ChIJKWScmxa9oRQRVULpHyK7GVU',place)
	place.reward = str(40)
	pointsToSpend=''
	place.offerPoints=''
	place.offerText= ''
	place.description='Monument of Zeus'
	place.questOrder=str(1)
	place.placeType="rewarding"
	places.append(place)

	place=Place()
	place=getDetailsForID('ChIJBznR1CK9oRQRgvc6KPVdI-c',place)
	place.reward = ''
	pointsToSpend='8'
	place.offerPoints=str(pointsToSpend)
	place.offerText= 'Free cake with your coffee , consuming ' + pointsToSpend + ' points'
	place.description='Cafe place'
	place.questOrder=str(2)
	place.placeType="consuming"
	places.append(place)

	return places		