from django.urls import include, path
from Coding import views

urlpatterns = [
    path('', views.index),#Default view/page
    path('index/', views.index, name='index'),

    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2')
]