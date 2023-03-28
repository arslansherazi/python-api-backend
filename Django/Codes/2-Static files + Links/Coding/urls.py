from django.urls import path
from Coding import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('page1', views.page1, name='page1'),
    path('page2', views.page2, name='page2')
]