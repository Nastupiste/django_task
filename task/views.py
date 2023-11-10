from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View
# Create your views here.


class Task_list(View):
    tasks = Task.objects.all()
    template_task = 'task_list.html'

    def actualizarTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_task, {'tasks': self.actualizarTask(), 'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.template_task, {'tasks': self.actualizarTask(), 'form': form})


"""
def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})
"""
