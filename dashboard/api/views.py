from rest_framework import generics, viewsets, permissions
from ..models import TodoDb
from .serializers import TodoDbSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoDb.objects.all()
    serializer_class = TodoDbSerializer
    permission_classes = [permissions.IsAuthenticated]

