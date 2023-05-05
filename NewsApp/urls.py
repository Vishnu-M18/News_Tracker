from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  #add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainApp.urls')), #add
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]