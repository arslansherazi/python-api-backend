from django.urls import include, path

from mongodb_client import apis

urlpatterns = [
    # apis routing
    path('add_student', apis.add_student),
    path('get_all_students', apis.get_all_students),
    path('delete_student', apis.delete_student),
    path('update_student', apis.update_student)
]
