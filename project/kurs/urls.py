from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register_view, name='register'),
    path('logging/', views.logging_view, name = 'logging'),

]