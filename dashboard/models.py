from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Complate_task(models.Model):
    
    users_complate = models.ForeignKey(
      User,
      on_delete=models.CASCADE
      )
    date_add = models.DateTimeField(
        auto_now_add=True
        )
        
    complate = models.BooleanField(default=False)
    
    def str(self):
        return self.users_complate
        
    class Meta:
        verbose_name = 'Закінчена задача'
        verbose_name_plural = 'Закінчені задачі'
        ordering = ['date_add']
    
class Cancel_task(models.Model):
    
    users_cancel = models.ForeignKey(
      User,
      on_delete=models.CASCADE
      )
      
    date_add = models.DateTimeField(
        auto_now_add=True
        )
        
    complate = models.BooleanField(default=False)
    
    def str(self):
        return self.header
        
    class Meta:
        verbose_name = 'Отмена'
        verbose_name_plural = 'Отмена'
        ordering = ['date_add']
        
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
        
    complate = models.ForeignKey(
        Complate_task, 
        on_delete=models.CASCADE, 
        default= None
        )
        
        
    cancel = models.ForeignKey(
        Cancel_task, 
        on_delete=models.CASCADE,
        default=None
        )

    def get_absolute_url(self):
        return reverse('dashboard:detail', kwargs={'pk': self.pk})
    
    def str(self):
        return self.header
        
    class Meta:
        verbose_name = 'Todoшка'
        verbose_name_plural = 'Todoшки'
        ordering = ['date_add']

