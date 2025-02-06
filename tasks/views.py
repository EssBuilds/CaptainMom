from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import TaskForm, ChildForm
from .models import Task, Child

@login_required
def home(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'home.html', {'children': children})

@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.user = request.user
            child.save()
            return redirect('home')
    else:
        form = ChildForm()
    return render(request, 'add_child.html', {'form': form})

@login_required
def task_detail(request, child_id):
    child = get_object_or_404(Child, id=child_id, user=request.user)
    tasks = Task.objects.filter(child=child)
    return render(request, 'task_detail.html', {'child': child, 'tasks': tasks})

@login_required
def add_task(request, child_id):
    child = get_object_or_404(Child, id=child_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.child = child
            task.save()
            return redirect('task_detail', child_id=child.id)
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form, 'child': child})