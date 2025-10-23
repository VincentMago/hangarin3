"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from hangarincore.views import (
    HomePageView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', HomePageView.as_view(), name='home'),
    path("accounts/", include("allauth.urls")), # allauth routes

    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='tasks-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='tasks-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks-delete'),

    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='categories-create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='categories-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='categories-delete'),

    path('priorities/', PriorityListView.as_view(), name='priorities-list'),
    path('priorities/create/', PriorityCreateView.as_view(), name='priorities-create'),
    path('priorities/<int:pk>/edit/', PriorityUpdateView.as_view(), name='priorities-update'),
    path('priorities/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priorities-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
       template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
