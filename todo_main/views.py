from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_task = Task.objects.filter(is_completed = True)
    context = {
        "tasks":tasks,
        "completed_task":completed_task,
    }
    return render(request,'home.html',context)