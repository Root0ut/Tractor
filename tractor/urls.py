from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('evidence/', include('evidence.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':tractor.settings.base.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':tractor.settings.base.STATIC_ROOT}),

]