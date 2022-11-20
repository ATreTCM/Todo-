from django.contrib import admin
from .models import TodoDb, Complate_task, Cancel_task


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
    
class ComplateAdmin(admin.ModelAdmin):
    list_display = (
        'users_complate',
        'date_add', 
       
        )

class CancelAdmin(admin.ModelAdmin):
    
    list_display = (
        'users_cancel',
        'date_add', 
     
        )


admin.site.register(TodoDb, TodoDBAdmin)
admin.site.register(Complate_task, ComplateAdmin)
admin.site.register(Cancel_task, CancelAdmin)
