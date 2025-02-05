# filepath: tasks/models.py
from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    name = models.CharField(max_length=100)
    mother = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return self.title