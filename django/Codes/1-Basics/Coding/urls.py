from django.urls import include, path
from Coding import views

urlpatterns = [
    path('', views.index),#used for index view/page (when user just enter url of website).Only one such path is possible among all applications
    path('index/', views.index),#used for index view/page (when user enter path for index page instead of just url of website)
]