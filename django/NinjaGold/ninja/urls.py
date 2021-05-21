from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    
    path('process_money',views.index),
    path('clear', views.clear),
]
