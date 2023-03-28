from django.conf.urls import include, url
from Guest import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
						#Practice
    url(r'^firstPage/',views.firstPage, name = 'firstPage'),
	#url(r'^urlParameters/(\d+)/(\d+)',views.urlParameters, name = 'urlParameters'),
	url(r'^urlParameters/(\d{2})/(\d{4})',views.urlParameters, name = 'urlParameters'), #specific length of parameters
	url(r'^hello/',views.hello, name = 'hello'),
	
	
	#web pages views
	 url(r'^index/',views.index, name = 'index'),
	 url(r'^register/',views.register, name = 'register'),
	 url(r'^faqs/',views.faqs, name = 'faqs'),
	 url(r'^friend/',views.friend, name = 'friend'),
	 url(r'^feedback/',views.feedback, name = 'feedback'),
	 url(r'^guestLogin/',views.guestLogin, name = 'guestLogin'),

	#forms handling views
	 url(r'^registerUser/', views.registerUser, name='registerUser'),
	 url(r'^tellAFriend/', views.tellAFriend, name='tellAFriend'),
	 url(r'^login/', views.login, name='guest_login_form'),
	 url(r'^feedbackForm/', views.feedbackForm, name='feedbackForm'),
	 url(r'^busSchedule/', views.busSchedule, name='busSchedule'),
	 url(r'^fares/', views.fares, name='fares'),
	 url(r'^checkUsername/(\d+)/', views.checkUsername, name='checkUsername'),
	 url(r'^loader/', views.loader, name='loader'),
]

urlpatterns += staticfiles_urlpatterns()
