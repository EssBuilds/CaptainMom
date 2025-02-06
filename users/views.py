from django.shortcuts import render

# Create your views here.
# filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/users/views.py

from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ParentRegistrationForm

def register_parent(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to Mom's Helper")
            return redirect('dashboard')
        messages.error(request, "Registration failed. Please check the form.")
    else:
        form = ParentRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})