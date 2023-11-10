from django.urls import path
from .views import *

urlpatterns = [
    path('', Task_list.as_view(), name='task_list'),
]
