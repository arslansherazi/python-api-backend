from django.urls import path

from apis import apis

urlpatterns = [
    # apis' views
    path('', apis.StudentApis.as_view()),
]
