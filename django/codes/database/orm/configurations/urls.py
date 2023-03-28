from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # apis' urls
    path('apis/', include('queries.urls')),
]
