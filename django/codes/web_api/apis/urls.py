from django.urls import include, path

from apis import views

urlpatterns = [
    # apis' views
    path('get_student', views.get_student),
    path('api', views.StudentApis.as_view()),
]