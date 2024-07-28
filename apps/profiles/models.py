from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class UserNotification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications_from_profiles', on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.content[:20]}"

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=5)

    def __str__(self):
        return f"{self.name} ({self.profile.user.username})"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company} ({self.profile.user.username})"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} ({self.profile.user.username})"

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return f"{self.platform} ({self.profile.user.username})"

class Connection(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='connections_sent', on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, related_name='connections_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_profile.user.username} to {self.to_profile.user.username} (Accepted: {self.accepted})"

class ProfileView(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_views', on_delete=models.CASCADE)
    viewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='viewed_profiles', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.profile.user.username} viewed by {self.viewed_by.username} at {self.timestamp}"
