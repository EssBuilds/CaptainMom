# filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/users/urls.py

from django.urls import path
from .views import register_parent

urlpatterns = [
    path('register/', register_parent, name='register'),
]