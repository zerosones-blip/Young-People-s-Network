from django.contrib import admin
from .models import Profile, Skill, Experience, Education, SocialLink, Connection, ProfileView

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'created_at', 'updated_at')
    search_fields = ('user__username', 'location')
    list_filter = ('created_at', 'updated_at')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'proficiency')
    search_fields = ('profile__user__username', 'name')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'company', 'start_date', 'end_date')
    search_fields = ('profile__user__username', 'title', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date')
    search_fields = ('profile__user__username', 'institution', 'degree', 'field_of_study')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('profile', 'platform', 'link')
    search_fields = ('profile__user__username', 'platform')

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('from_profile', 'to_profile', 'created_at', 'accepted')
    search_fields = ('from_profile__user__username', 'to_profile__user__username')
    list_filter = ('accepted', 'created_at')

@admin.register(ProfileView)
class ProfileViewAdmin(admin.ModelAdmin):
    list_display = ('profile', 'viewed_by', 'timestamp')
    search_fields = ('profile__user__username', 'viewed_by__username')
    list_filter = ('timestamp',)
