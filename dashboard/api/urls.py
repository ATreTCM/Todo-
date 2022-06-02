from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'dashboard'

router = routers.DefaultRouter()
router.register(r'tasks', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]