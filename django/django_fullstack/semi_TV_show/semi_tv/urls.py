from django.urls import path, include
from . import views

urlpatterns = [
   path('shows',views.shows),
   path('',views.index), 
   path('shows/new',views.create),
   path('shows/add',views.add),
   path('shows/<int:id>',views.read),
   path('shows/<int:id>/edit', views.update),
   path('<int:id>', views.edit),
   path('destroy/<int:id>',views.destroy),


]
