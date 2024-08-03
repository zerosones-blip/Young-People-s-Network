from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.profile.models import Profile

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=510)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    shared_from = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='shares')

    def __str__(self):
        return f"{self.author.username}'s post at {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=510)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.author.username}'s post"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name

class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='views')
    viewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='viewed_posts')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.post.author.username}'s post viewed by {self.viewed_by.username} at {self.timestamp}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications_from_posts', on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.content[:20]}"
