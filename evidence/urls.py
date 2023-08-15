from django.urls import path
from . import views
app_name='evidence'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('<int:pk>', views.detail, name='detail'),
]