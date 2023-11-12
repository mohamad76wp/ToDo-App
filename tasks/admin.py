from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'create',)
    list_filter = ('complete', 'create',)
    search_fields = ('title',)