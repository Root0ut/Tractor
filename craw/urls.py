from django.urls import path

from . import views

app_name = 'craw'

urlpatterns = [
    path('', views.index),
    path('craw_list/', views.craw_list, name='craw_list'),
    path('tractor_main/', views.tractor_main, name='tractor_main'),
]