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
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'
    paginate_by = 5
    
    def get_ordering(self):
        allowed = ["title", "status", "deadline", "category__name", "priority__name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "deadline"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(status__icontains=query) |
                Q(category__name__icontains=query) |
                Q(priority__name__icontains=query)
            )
        return qs

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks_create.html'
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    success_url = reverse_lazy('tasks-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks_create.html'
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    success_url = reverse_lazy('tasks-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks_del.html'
    success_url = reverse_lazy('tasks-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories_create.html'
    fields = ['name']
    success_url = reverse_lazy('categories-list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories_create.html'
    fields = ['name']
    success_url = reverse_lazy('categories-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories_del.html'
    success_url = reverse_lazy('categories-list')


class PriorityListView(ListView):
    model = Priority
    template_name = 'priorities_list.html'
    context_object_name = 'priorities'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(name__icontains=query))
        return qs

class PriorityCreateView(CreateView):
    model = Priority
    template_name = 'priorities_create.html'
    fields = ['name']
    success_url = reverse_lazy('priorities-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    template_name = 'priorities_create.html'
    fields = ['name']
    success_url = reverse_lazy('priorities-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priorities_del.html'
    success_url = reverse_lazy('priorities-list')
