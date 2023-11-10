"""
Modelo
"""
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
