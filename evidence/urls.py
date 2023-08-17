from django.urls import path
from . import views
app_name='evidence'

urlpatterns = [
    path('', views.lists, name='lists'),
    path('lists/', views.lists, name='lists'),
    path('write/', views.write, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('get_second_pw/', views.get_second_pw, name='get_second_pw'),

]
