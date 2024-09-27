from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('',  views.index),
    path('add/', views.add),
    path('Save/', views.Save),
    path('delete/<int:id>/', views.delete),
    path('update/<int:id>/', views.update),
    path('edit/<int:id>/', views.edit),
]
