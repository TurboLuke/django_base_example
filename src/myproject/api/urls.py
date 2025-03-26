from django.urls import include, path
from rest_framework import routers

from  . import views 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('todos/', views.todos, name='todos'),
    path('todos/create/', views.todo_create, name='todo_create'),
]