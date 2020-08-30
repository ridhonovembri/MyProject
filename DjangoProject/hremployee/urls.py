from django.urls import path

from . import views

urlpatterns = [
    path('/', views.index),
    path('/add/', views.add),
    path('/update/', views.update),
    path('/delete/', views.delete),

]