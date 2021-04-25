from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm
# Create your views here.
def homepage(request):
    form = TaskForm()
    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"form": form, "tasks": tasks}
    return render(request, "task_list.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    if(task.complete):
        task.complete = False
    else:
        task.complete = True
    task.save()
    return redirect('/')

    

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    Task.delete(task)
    return redirect('/')
    