from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_default_user():
    User = get_user_model()
    return User.objects.first().id  # Returns the ID of the first user in the database

class Child(models.Model):
    parent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=get_default_user  # Use a callable function for dynamic assignment
    )
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default='2000-01-01')  # Add a default value
    favorite_toy = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return f"{self.title} - {self.child.name}"

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title