from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todos.models import Task


def addTask(request):
    task = request.POST['task']
    addtask = Task.objects.create(task = task)
    return redirect('home')

def markas_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markas_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
           "get_task":get_task, 
        }
    return render(request,'edit_task.html',context)

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')