from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Coding.urls')),
    path('Coding/', include('Coding.urls'))
]
