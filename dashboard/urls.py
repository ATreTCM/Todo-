from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('<int:pk>/update', views.TdUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.TdDeleteView.as_view(), name='delete'),
    path('', views.TdListView.as_view(), name='list'),
    path('<int:pk>', views.TdDetailView.as_view(), name='detail'),
    path('create/', views.createView, name='create'),
]
