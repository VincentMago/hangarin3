from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hangarincore.models import Task, Category, Priority


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_count'] = Task.objects.count()
        context['categories_count'] = Category.objects.count()
        context['priorities_count'] = Priority.objects.count()
        return context


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'  
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/tasks_create.html'
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    success_url = reverse_lazy('tasks-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/tasks_create.html'
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    success_url = reverse_lazy('tasks-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/tasks_del.html'
    success_url = reverse_lazy('tasks-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/categories_create.html'
    fields = ['name']
    success_url = reverse_lazy('categories-list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories/categories_create.html'
    fields = ['name']
    success_url = reverse_lazy('categories-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/categories_del.html'
    success_url = reverse_lazy('categories-list')


class PriorityListView(ListView):
    model = Priority
    template_name = 'priorities/priorities_list.html'
    context_object_name = 'priorities'

class PriorityCreateView(CreateView):
    model = Priority
    template_name = 'priorities/priorities_create.html'
    fields = ['name']
    success_url = reverse_lazy('priorities-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    template_name = 'priorities/priorities_create.html'
    fields = ['name']
    success_url = reverse_lazy('priorities-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priorities/priorities_del.html'
    success_url = reverse_lazy('priorities-list')
