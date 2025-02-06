# filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_parent = models.BooleanField(default=True)
    profile_color = models.CharField(max_length=7, default='#ff9966')