from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin



class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_list.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_list.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'todo/task_list.html'
    success_url = reverse_lazy('task_list')
    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_detail.html'

def task_search(request):
    query = request.GET.get('query', '')
    tasks = Task.objects.filter(title__icontains=query, user=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'search_query': query})
