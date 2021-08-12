from django.urls import path

from apis.add_student.api import AddStudent
from apis.add_course.api import AddCourse
from apis.assign_course.api import AssignCourse
from apis.get_students_info.api import GetStudentsInfo

urlpatterns = [
    path('add_student', AddStudent.as_view()),
    path('get_students_info', GetStudentsInfo.as_view()),
    path('add_course', AddCourse.as_view()),
    path('assign_course', AssignCourse.as_view())
]
