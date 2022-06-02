from rest_framework import serializers
from ..models import TodoDb


class TodoDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDb
        fields = [
            'author',
            'header',
            'content',
            'slave',
            'photo',
                  ]


