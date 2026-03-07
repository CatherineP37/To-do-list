from django.shortcuts import render, redirect
from .models import TaskList
from .forms import AddTask

def home(request):
    tasks = TaskList.objects.all()
    form = AddTask()
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')        
    context = {'form':form, 'tasks':tasks}
    return render(request, 'home.html', context)
