from django.urls import include, path
from Coding import views

urlpatterns = [
    path('', views.index),#Default view/page
    path('index', views.index),

    path('addBook', views.addBook, name='addBook'),
    path('addBookSuccess', views.addBookSuccess, name='addBookSuccess'),
    path('addBookForm', views.addBookForm, name='addBookForm'),
    path('viewBooks', views.viewBooks, name='viewBooks'),
    path('updateDelete', views.updateDelete, name='updateDelete'),
    path('updateBook', views.updateBook, name='updateBook'),
    path('updateBookForm', views.updateBookForm, name='updateBookForm'),
]