# filepath: /c:/Users/ekari/OneDrive/Desktop/FINAL PROJECT/new_todoapp/tasks/urls.py
from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    login_view, logout_view, todo_list, todo_detail, child_list, child_detail
)

urlpatterns = [
    # Class-based views for tasks
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

    # API views for authentication, todos, and children
    path('api/login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/todos/', todo_list, name='todo_list'),
    path('api/todos/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('api/children/', child_list, name='child_list'),
    path('api/children/<int:child_id>/', child_detail, name='child_detail'),
]