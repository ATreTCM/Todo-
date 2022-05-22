from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import TodoDb


class TodoDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDb
        fields = ['header',
                  'content',
                  'slave',
                  'photo',
                  ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url',
                  'username',
                  'email',
                  'is_staff',
                  ]