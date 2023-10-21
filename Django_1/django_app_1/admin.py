from django.contrib import admin
from .models import Task, Project


class TaskInline(admin.TabularInline):
    model = Task


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'status', 'priority']
    list_filter = ['status', 'priority']


admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)

