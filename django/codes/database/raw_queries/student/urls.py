from django.urls import path

from student.apis.add_student import AddStudent
from student.apis.delete_student import DeleteStudent
from student.apis.get_all_students import GetAllStudents
from student.apis.get_particular_student import GetParticularStudent1
from student.apis.get_student_by_degree_and_cgpa import GetParticularStudent2
from student.apis.update_student import UpdateStudent

urlpatterns = [
    path('add_student', AddStudent.as_view()),
    path('delete_student', DeleteStudent.as_view()),
    path('get_all_students', GetAllStudents.as_view()),
    path('get_particular_student', GetParticularStudent1.as_view()),
    path('get_particular_student_by_degree_and_cgpa', GetParticularStudent2.as_view()),
    path('update_student', UpdateStudent.as_view()),
]