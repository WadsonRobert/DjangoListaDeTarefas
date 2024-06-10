from django.contrib import admin
from tasks.models import Completed, Task

# # Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'feita')
    search_fields = ('titulo',)

class CompletedAdmin(admin.ModelAdmin):
    list_display = ('id', 'opcoes',)
    search_fields = ('opcoes',)


admin.site.register(Completed, CompletedAdmin)
admin.site.register(Task, TaskAdmin)