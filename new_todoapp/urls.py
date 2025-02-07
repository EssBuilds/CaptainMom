from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Redirect root URL to the task list
    path('', RedirectView.as_view(url=reverse_lazy('task-list')), name='root-redirect'),

    # Admin site
    path('admin/', admin.site.urls),

    # Task-related URLs
    path('tasks/', include([
        path('', TaskListView.as_view(), name='task-list'),
        path('create/', TaskCreateView.as_view(), name='task-create'),
        path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
        path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    ])),

    # API URLs
    path('api/', include('tasks.urls')),

    # Users app
    path('users/', include('users.urls')),

    # Login and logout views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]