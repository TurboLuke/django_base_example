from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItem

# Create your views here.

def home(request): # name of the view
    # return hello world
    return render(request, 'home.html') # render the template

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {
        'todos': items
    })  
