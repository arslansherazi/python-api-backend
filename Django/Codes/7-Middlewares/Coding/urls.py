from django.urls import path
from Coding import views

urlpatterns = [
    path('get_response', views.get_response),
]
