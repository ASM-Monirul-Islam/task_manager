from django.contrib import admin
from . models import Task
# Register your models here.
@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
	list_display = ('user', 'title', 'is_completed', 'description', 'created_at')
	list_filter = ('user', 'is_completed')
	search_fields = ('user', 'title')