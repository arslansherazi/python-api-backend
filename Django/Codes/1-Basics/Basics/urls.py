from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Coding.urls')),#used for index page/view of Coding application (Only one view of any application can be chosen as index view/page)
    path('Coding/', include('Coding.urls')),#used for other views/pages of Coding application
]
