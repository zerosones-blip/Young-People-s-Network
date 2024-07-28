from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserNotification

@receiver(post_save, sender=CustomUser)
def create_welcome_notification(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.create(user=instance, content="Welcome to Young people's Network!")
