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
    
    # filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/tasks/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import Todo, Child
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'})

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todos = list(Todo.objects.values())
        return JsonResponse(todos, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        todo = Todo.objects.create(**data)
        return JsonResponse(todo.to_dict())

@csrf_exempt
def todo_detail(request, todo_id):
    if request.method == 'DELETE':
        Todo.objects.filter(id=todo_id).delete()
        return JsonResponse({'message': 'Todo deleted'})

@csrf_exempt
def child_list(request):
    if request.method == 'GET':
        children = list(Child.objects.values())
        return JsonResponse(children, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        child = Child.objects.create(**data)
        return JsonResponse(child.to_dict())

@csrf_exempt
def child_detail(request, child_id):
    if request.method == 'DELETE':
        Child.objects.filter(id=child_id).delete()
        return JsonResponse({'message': 'Child deleted'})