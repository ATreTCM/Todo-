from rest_framework import serializers
from todolist.dashboard.models import TodoDb


class TodoDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDb
        fields = ['header',
                  'content',
                  'slave',
                  'photo',
                  ]