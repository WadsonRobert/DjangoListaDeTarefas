from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskForm
# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'Task.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        tasks = super().get_queryset().order_by('data')
        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(titulo__icontains=search)
        return tasks
    
class NewTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'Newtask.html'
    success_url = '/'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update_form.html'
    success_url = reverse_lazy('tasks_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy("tasks_list")



    
    
