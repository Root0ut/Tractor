from django.urls import path
from . import views
app_name='legalsite'

urlpatterns = [
    path('', views.index, name='index'),
]
