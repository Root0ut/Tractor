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
]