from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.home),
    path('notes', views.note),
    path('save', views.save),
    path('delete',views.delete),
    path('create',views.create1),
    path('savenew',views.savenew)
]