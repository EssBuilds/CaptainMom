from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, ChildListView, ChildCreateView, ChildUpdateView, ChildDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('children/', ChildListView.as_view(), name='child-list'),
    path('children/create/', ChildCreateView.as_view(), name='child-create'),
    path('children/<int:pk>/update/', ChildUpdateView.as_view(), name='child-update'),
    path('children/<int:pk>/delete/', ChildDeleteView.as_view(), name='child-delete'),
]