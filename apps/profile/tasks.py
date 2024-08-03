from celery import shared_task
from django.core.mail import send_mail
from .models import Connection

@shared_task
def send_connection_request_email(connection_id):
    connection = Connection.objects.get(id=connection_id)
    send_mail(
        f'New Connection Request from {connection.from_profile.user.username}',
        f'You have a new connection request from {connection.from_profile.user.username}.',
        'noreply@example.com',
        [connection.to_profile.user.email]
    )
