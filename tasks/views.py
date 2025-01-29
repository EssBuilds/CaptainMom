from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, TaskCategory, Child

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'category', 'priority', 'child']
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'category', 'priority', 'child']
    template_name = 'tasks/task_form.html'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = 'tasks/task_confirm_delete.html'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user

class ChildListView(LoginRequiredMixin, ListView):
    model = Child
    template_name = 'tasks/child_list.html'
    context_object_name = 'children'
    
    def get_queryset(self):
        return Child.objects.filter(mother=self.request.user)

class ChildCreateView(LoginRequiredMixin, CreateView):
    model = Child
    fields = ['name', 'age']
    template_name = 'tasks/child_form.html'

    def form_valid(self, form):
        form.instance.mother = self.request.user
        return super().form_valid(form)

class ChildUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Child
    fields = ['name', 'age']
    template_name = 'tasks/child_form.html'

    def test_func(self):
        child = self.get_object()
        return self.request.user == child.mother

class ChildDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Child
    success_url = '/children/'
    template_name = 'tasks/child_confirm_delete.html'

    def test_func(self):
        child = self.get_object()
        return self.request.user == child.mother