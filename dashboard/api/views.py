from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from ..models import TodoDb
from .serializers import TodoDbSerializer, UserSerializer


class TodoDbListView(generics.ListAPIView):
    queryset = TodoDb.objects.all()
    serializer_class = TodoDbSerializer


class TodoDbDetailView(generics.RetrieveAPIView):
    queryset = TodoDb.objects.all()
    serializer_class = TodoDbSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]