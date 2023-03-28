from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from Coding import views


urlpatterns = [
    path('get_student', views.get_student),
    path('register_student', views.register_student),
    path('api', views.StudentApis.as_view()),

    path('api/token', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view()),
]