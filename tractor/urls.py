
from django.contrib import admin
from django.urls import path, include
from tractor import views
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from tractor import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('evidence/', include('evidence.urls')),
    path('', views.index, name='index'),  
]


