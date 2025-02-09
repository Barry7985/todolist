from django.urls import path
from .views import TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, task_filter, task_search

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/edit/', TaskDetailView.as_view(), name='task_edit'),
    path('filter/<str:filter_type>/',task_filter, name='task_filter'),
    path('search/', task_search, name='task_search'),
]
