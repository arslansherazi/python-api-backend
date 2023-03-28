from django.urls import path
from Coding import views

urlpatterns = [
    path('', views.index),#Default page/url
    path('index', views.index),
    path('form1', views.form1, name='form1'),
    path('form2', views.form2, name='form2'),
    path('success1', views.success1, name='success1'),
    path('success2', views.success2, name='success2'),

    path('form1Handling', views.form1Handling, name='form1Handling'),
    path('form2Handling', views.form2Handling, name='form2Handling'),
]