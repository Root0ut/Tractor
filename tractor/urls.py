from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import re_path as url
from django.views.static import serve
from tractor import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('evidence/', include('evidence.urls')),
    path('hello/', views.index),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),

]