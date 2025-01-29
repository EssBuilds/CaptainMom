from django.db import models
from users.models import CustomUser

class TaskCategory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # Hex color

class Child(models.Model):
    mother = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    is_complete = models.BooleanField(default=False)
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)