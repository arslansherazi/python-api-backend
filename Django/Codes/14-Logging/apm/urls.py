from django.urls import path

from apm import views


urlpatterns = [
    path('', views.division),
]
