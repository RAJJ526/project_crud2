from django.contrib import admin
from django.urls import path, include
from my_app2 import views
urlpatterns = [
    path('', views.home),
    path('new/', views.add),
    path('Save/', views.Save),
    path('delete/<int:id>/', views.delete),
    path('change/<int:id>/', views.change),
    path('update/<int:id>/', views.update),

]