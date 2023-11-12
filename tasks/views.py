from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import TasksForm
from .models import Task
# Create your views here.

def index(request):
    data = Task.objects.all()
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'data':data, 'form':form}
    return render(request, 'tasks/index.html', context)


def updateTask(request,pk):     
    task = Task.objects.get(id=pk)

    form = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if 'complete' in request.POST:
            task.complete = True
        else:
            task.complete = False
        if form.is_valid():
            form.save()  # Save the form data
            return redirect('/')
    context = {'form':form}

    return render(request,'tasks/update_task.html',context)



def deteleTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')