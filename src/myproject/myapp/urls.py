from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #root
    path('todos/', views.todos, name='todos'), #todos
]