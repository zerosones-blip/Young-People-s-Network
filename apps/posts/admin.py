from django.contrib import admin
from .models import Post, Comment, Tag, PostView, Notification

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'updated_at')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content', 'created_at', 'updated_at')
    search_fields = ('author__username', 'post__content', 'content')
    list_filter = ('created_at', 'updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'viewed_by', 'timestamp')
    search_fields = ('post__content', 'viewed_by__username')
    list_filter = ('timestamp',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'read', 'timestamp')
    list_filter = ('read', 'timestamp')