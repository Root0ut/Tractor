from django.urls import path

from . import views

app_name='pdfextract'

urlpatterns = [
    path('',views.index, name='index'),
    path('storage/', views.storage, name='storage'),
    path('create/', views.create, name='create'),
    path('extract/', views.extract, name='extract'),
    path('download/', views.download, name='download'),
]