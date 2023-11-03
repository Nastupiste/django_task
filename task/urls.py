from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.task_list, name='task_list'),
]
