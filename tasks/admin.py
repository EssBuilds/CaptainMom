from django.contrib import admin
from .models import Task, Child, Todo

# Register your models here.
admin.site.register(Task)
admin.site.register(Child)
admin.site.register(Todo)