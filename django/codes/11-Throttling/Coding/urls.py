from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from Coding import views


urlpatterns = [
    # urls for jwt tokens
    path('api/token', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view()),

    # urls for generic apis
    path('register_company', views.register_company),
    path('api/subscription1', views.CompanyApisSubscription1.as_view()),
    path('api/subscription2', views.CompanyApisSubscription2.as_view()),
]