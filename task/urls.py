from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task/<int:pk>', TaskDescription.as_view(), name='task_description'),
    path('task/new', NewTask.as_view(), name='formulario')
]
