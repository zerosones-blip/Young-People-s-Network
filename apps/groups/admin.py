from django.contrib import admin
from .models import Group, Membership

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'date_joined')
    search_fields = ('user__username', 'group__name')
