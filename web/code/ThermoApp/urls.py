from django.conf.urls import url
from ThermoApp import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
	#url(r'^name/', views.get_name, name ='get_name'),
    url(r'^userinterface/', views.UserInterface, name ='UserInterface'),
    #url(r'^updateuserinterface/([0-9]{2})', views.updateuserinterface, name ='updateuserinterface'),  #expects a numberic value at the end
    url(r'^updateuserinterface/', views.UserInterface, name ='UserInterface'),
    url(r'^(?P<hsduration>[0-9]+)/historicinterface', views.historicinterface, name ='historicinterface'),
    url(r'^historicinterface/(?P<hsduration>[0-9]+)', views.historicinterface, name ='historicinterface'),
    url(r'^historicinterface/', views.historicinterface, name ='historicinterface'),
    url(r'^automationinterface/', views.automationinterface, name ='automationinterface'),
	url(r'^development/', views.developmentinterface, name ='development'),
    ]