from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('coding.urls')),#used for index page/view of coding application (Only one view of any application can be chosen as index view/page)
    path('coding/', include('coding.urls')),#used for other views/pages of coding application
]
