from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Notification

@receiver(post_save, sender=Post)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        # Example: Create a notification for all followers of the post author
        try:
            followers = instance.author.profile.followers.all()
        except AttributeError:
            pass
        else:
            for follower in followers:
                Notification.objects.create(
                    user=follower.user,
                    post=instance,
                    message=f'New post from {instance.author.username}',
                )
