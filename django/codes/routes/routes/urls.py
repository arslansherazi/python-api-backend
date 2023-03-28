from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    #If we use only the following pattern then we can only access view/page using syntax "domain/view_path"
    path('', include('coding.urls')),

    ##If we use only the following pattern then we can access view/page using syntax "domain/view_path" and also "domain/AppName(We can change name but app name is recommended)/view_path"
    #path('coding/', include('coding.urls'))
]
