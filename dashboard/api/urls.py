from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'dashboard'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', views.TodoDbListView.as_view(), name='todo_list'),
    path('tasks/<pk>/', views.TodoDbDetailView.as_view(), name='todo_detail'),
    ]