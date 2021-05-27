from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('create',views.create),
    path('success',views.welcome),
    path('login',views.login),
    path('logout',views.logout)
    
]