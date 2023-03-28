from django.urls import path
from Coding import views

urlpatterns = [
    path('', views.index),#Default page/url
    path('index', views.index),

    path('loginForm', views.loginForm, name='loginForm'), 
    path('logout', views.logout, name='logout'), 
    path('loggedinPage', views.loggedinPage, name='loggedinPage'),  
]