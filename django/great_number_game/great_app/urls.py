from django.urls import path     
from . import views
urlpatterns = [
    path('', views.theprime),
    path('post', views.index),
]