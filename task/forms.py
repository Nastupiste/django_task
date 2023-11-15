from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']


"""
class TaskForm(forms.Form):
    title = forms.CharField(label="Título:", max_length=100)
    description = forms.CharField(label="Descripción:", widget=forms.Textarea)
    completed = forms.BooleanField(label="Completada:", required=False)
"""
