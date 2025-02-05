# filepath: tasks/forms.py
from django import forms
from .models import Task, Child

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'child']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name']