from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.utils.timezone import now

# Custom User Model
class CustomUser(AbstractUser):
    is_parent = models.BooleanField(default=True)
    profile_color = models.CharField(
        max_length=7,
        default='#ff9966',
        validators=[RegexValidator(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', 'Enter a valid hex color code.')]
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

# Child Model
class Child(models.Model):
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_children')
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def clean(self):
        if self.birth_date > date.today():
            raise ValidationError("Birth date cannot be in the future.")

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return self.name

# Task Model
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

    @property
    def is_overdue(self):
        return not self.completed and self.due_date < now()

    def __str__(self):
        return f"{self.title} - {self.child.name}"

# Todo Model
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def clean(self):
        if self.due_date < date.today():
            raise ValidationError("Due date cannot be in the past.")

    def __str__(self):
        return self.title