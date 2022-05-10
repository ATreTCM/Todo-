from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TodoDb(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    slave = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse('dashboard:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date_add']

