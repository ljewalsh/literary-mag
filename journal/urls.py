from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls)    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)