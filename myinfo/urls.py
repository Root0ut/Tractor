from django.urls import path
from . import views
app_name='myinfo'

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
]
