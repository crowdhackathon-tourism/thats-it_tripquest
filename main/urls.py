from django.conf.urls import url, patterns,include
from backend import views

urlpatterns = patterns(
	url(r'^backend/', views.search),
	url(r'^search/(?P<query>[^/]+)/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/$', views.search),
	url(r'^search/(?P<query>[^/]+)/$', views.simpleSearch),
	url(r'^search/rewarding/(?P<query>[^/]+)/$', views.searchRewarding),
	url(r'^search/consuming/(?P<query>[^/]+)/$', views.searchConsuming),
	url(r'^quest/(?P<questID>\d+)/$', views.quest),
	url(r'^quests/', views.quests)
)
