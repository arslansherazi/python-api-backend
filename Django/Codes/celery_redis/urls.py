from django.urls import path

from apis.add_student.api import AddStudent

urlpatterns = [
    path('add_student', AddStudent.as_view())
]
