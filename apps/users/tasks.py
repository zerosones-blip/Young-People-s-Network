from celery import shared_task
from django.core.mail import send_mail
from .models import UserNotification

@shared_task
def send_notification_email(notification_id):
    notification = UserNotification.objects.get(id=notification_id)
    send_mail(
        f'New Notification: {notification.notification_type}',
        notification.message,
        'noreply@example.com',
        [notification.user.email]
    )
