from django.db import models
from django.utils.timezone import now
from children.models import Child

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    child = models.ForeignKey('children.Child', on_delete=models.CASCADE)
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