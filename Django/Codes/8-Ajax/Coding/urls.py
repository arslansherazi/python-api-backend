from django.urls import path
from Coding import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),

    path("addStudent/", views.addStudent),
    path("noJS/", views.noJS, name="no_js"),
    path("getAllStudents/", views.getAllStudents),
    path("searchStudent", views.searchStudent),
    path("deleteStudent", views.deleteStudent),
    path("updateStudent", views.updateStudent)
]