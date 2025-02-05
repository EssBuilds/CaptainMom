# filepath: tasks/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Child
from .forms import TaskForm, ChildForm

@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.mother = request.user
            child.save()
            return redirect('child_list')
    else:
        form = ChildForm()
    return render(request, 'tasks/add_child.html', {'form': form})

@login_required
def delete_child(request, child_id):
    child = Child.objects.get(id=child_id, mother=request.user)
    if request.method == 'POST':
        child.delete()
        return redirect('child_list')
    return render(request, 'tasks/delete_child.html', {'child': child})

@login_required
def child_list(request):
    children = Child.objects.filter(mother=request.user)
    return render(request, 'tasks/child_list.html', {'children': children})