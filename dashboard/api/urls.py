from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('tasks/', views.TodoDbListView.as_view(), name='todo_list'),
    path('tasks/<pk>/', views.TodoDbDetailView.as_view(), name='todo_detail'),
    ]