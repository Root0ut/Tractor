from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from myinfo import views

from . import views
app_name='myinfo'

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/save_survey', views.save_survey, name='save_survey'),
]
