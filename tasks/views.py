# filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/tasks/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Child

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(child__parent=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['child', 'title', 'description', 'due_date', 'priority']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.child = form.cleaned_data['child']
        if form.instance.child.parent != self.request.user:
            form.add_error('child', 'Invalid child selection')
            return self.form_invalid(form)
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['child', 'title', 'description', 'due_date', 'priority']
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(child__parent=self.request.user)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(child__parent=self.request.user)