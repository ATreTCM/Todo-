from rest_framework import generics
from todolist.dashboard.models import TodoDb
from .serializers import TodoDbSerializer


class TodoDbListView(generics.ListAPIView):
    queryset = TodoDb.objects.all()
    serializer_class = TodoDbSerializer


class TodoDbDetailView(generics.RetrieveAPIView):
    queryset = TodoDb.objects.all()
    serializer_class = TodoDbSerializer
