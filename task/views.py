from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views import View
# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TaskForm


class Home(View):
    tasks = Task.objects.all()

    def actualizarTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        form = TaskForm()
        return render(request, 'home.html', {'tasks': self.actualizarTask(), 'form': form})


class NewTask(View):

    def get(self, request):
        form = TaskForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'form.html', {'form': form})


class TaskDescription(View):
    template_home = 'home_list.html'
    template_description = 'task_description.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, self.template_description, {'task': task})


class EditTask(View):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task_edit.html', {'task': task, 'form': form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            form.save()
            return redirect('task_description', pk=pk)
        return render(request, 'task_edit.html', {'task': task, 'form': form})


# Organizado en funciones (form.Form)


"""
class NewTask(View):
    tasks = Task.objects.all()

    def actualizarTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        form = TaskForm()
        return render(request, "task_list.html", {'tasks': self.actualizarTask(), "form": form})

    def post(self, request):
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                # process the data in form.cleaned_data as required
                title = form.cleaned_data["title"]
                description = form.cleaned_data["description"]
                completed = form.cleaned_data["completed"]
                Task.objects.create(
                    title=title, description=description, completed=completed)
                # redirect to a new URL:
                return HttpResponseRedirect("task_list")
            return render(request, "task_list.html", {'tasks': self.actualizarTask(), "form": form})


"""

# Organizado en funciones

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
