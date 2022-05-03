from .models import TodoDb
from django.forms import ModelForm


class TasksForm(ModelForm):
    class Meta:
        model = TodoDb
        fields = ['header',
                  'content',
                  'slave',
                  #'photo',
                  ]
