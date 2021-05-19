from django.urls import path     
from . import views
urlpatterns = [
    path('', (views.index)),
    path('to', (views.some_function)),
    path('to/destroy', (views.destroy)),
    path('to/plustwo', (views.plustwo)),
]