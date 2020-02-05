from django.urls import include, path
from Coding import views

urlpatterns = [
    path('', views.index),#Default view/page
    path('index', views.index, name='index'),

    path('loggedinPage', views.loggedinPage, name='loggedin_page'),
    path('loginForm', views.loginForm, name='login_form'),
    path('logout', views.logout, name='logout'),
]