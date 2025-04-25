from django.contrib import admin
from .models import Task, Date, UrgencyLevel, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'urgency')
    list_filter = ('urgency', 'tags')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(UrgencyLevel)
class UrgencyLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)