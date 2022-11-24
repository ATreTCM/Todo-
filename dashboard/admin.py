from django.contrib import admin
from .models import TodoDb


class TodoDBAdmin(admin.ModelAdmin):
    
    list_display = (
        'author',
        'header',
        'content',
        'slave',
        'date_add',
        'date_update',
        'photo',
        'complate',
        'cancel',     
        )
    list_filter = (
        'author',
        'date_add',
        'date_update',
        'complate',
        'cancel',
        'slave'
    )
    search_fields = (
        'author',
        'slave',
        'complate',
        'cancel',
        'date_add'
    )
    ordering = (
        'complate',
        'cancel',
    )
    


admin.site.register(TodoDb, TodoDBAdmin)
