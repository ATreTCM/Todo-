from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
        
class TodoDb(models.Model):
    """Таблица для поставленных задачь"""
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
        
    header = models.CharField(
        max_length=100, 
        verbose_name='Заголовок'
        )
        
    content = models.TextField(
        max_length=500,
        verbose_name='Задача'
        )
        
    slave = models.CharField(
        max_length=100, 
        verbose_name='Виконавець'
        )
        
    date_add = models.DateTimeField(
        auto_now_add=True
        )
        
    date_update = models.DateTimeField(
        auto_now=True
        )
        
    photo = models.ImageField(
        blank=True, 
        null=True, 
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='Фото'
        )
        
    complate = models.BooleanField(  
        default= False
        )
        
        
    cancel = models.BooleanField(  
        default= False
        )

    def get_absolute_url(self):
        return reverse('dashboard:detail', kwargs={'pk': self.pk})
    
    def str(self):
        return self.header
        
    class Meta:
        verbose_name = 'Todoшка'
        verbose_name_plural = 'Todoшки'
        ordering = ['date_add']

