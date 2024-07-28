from django.contrib import admin
from .models import Event, EventAttendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'group', 'created_by')
    search_fields = ('title', 'description', 'location', 'group__name', 'created_by__username')
    list_filter = ('start_time', 'end_time', 'group')

@admin.register(EventAttendance)
class EventAttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'timestamp')
    search_fields = ('event__title', 'user__username')
    list_filter = ('timestamp',)
