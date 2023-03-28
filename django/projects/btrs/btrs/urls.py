from django.conf.urls import url,include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^Admin/', include('Admin.urls'),name='Admin'),
    url(r'^User/', include('User.urls')),
    url(r'^Guest/', include('Guest.urls')), #"Guest" is an application of our project
]
