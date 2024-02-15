from django.contrib import admin

from todos.models import Task


# Register your models here.
class Taskadmin(admin.ModelAdmin):
    list_display = ('task','is_completed','is_updated')

admin.site.register(Task,Taskadmin)