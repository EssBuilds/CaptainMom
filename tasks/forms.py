from django import forms
from .models import Task, Child

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name']