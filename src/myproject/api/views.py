from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import TodoItem

# Create your views here.
from myapp.models import TodoItem

# CRUD todo items

# Create
@api_view(['POST'])
def todo_create(request):
    data = request.data
    TodoItem.objects.create(
        title=data['title'],
        completed=data['completed']
    )
    return Response({
        'message': 'Todo item created successfully!'
    })

# Read
@api_view(['GET'])
def todos(request):
    return Response({
        'todos': list(TodoItem.objects.values())
    })