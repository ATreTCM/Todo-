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
        )
    list_filter = (
        'author',
        'date_add',
        'date_update',
        'complate',
        'slave'
    )
    search_fields = (
        'author',
        'slave',
        'complate',
        'date_add'
    )
    ordering = (
        'complate',
    )
    


admin.site.register(TodoDb, TodoDBAdmin)
