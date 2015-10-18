

# Instructions for setting up TripQuest API #
The application was created and tested on Ubuntu, but the app can be set up on every operating system by running the following commands on the command line.

### Requirements: 
[Python 2.7.9 or above (from Python 2 versions)](https://www.python.org/downloads) 

Includes pip package manager(Note: you can also use previous python versions, but you must ensure that you also have pip package manager installed. 2.7.9 and above comes with pip included)

* Clone the existing project

* Navigate inside the cloned folder and run
`pip install -r requirements.txt`
(Note: For linux users: if you get access problems, try to run it as superuser. For windows users: You may need to add the path containing pip in your installation to your environment PATH variable. Any user: You can also use virtualenv, but is not necessary)

* After installing the dependencies, run the following sequence of commands:


`python manage.py createcachetable`

`python manage.py migrate`

`python manage.py runserver`

You must now have the API server up and running

You can view the Quests by typing http://localhost:8000/quests/
(Note that a convenient view created by django-rest-framework will be displayed. If you want to get the raw json, concatenate ?format=json to the end of the previous urls)

In case you want to clear the cache and the database, navigate to the base folder and run the command 
`python manage.py flush`

For the mobile app you need to get the [Ionic framework](http://ionicframework.com/) and then emulate/or run the app to your chosen devices. The code resides in the frontend folder. You can also view the created mockup views in the folder named views.


