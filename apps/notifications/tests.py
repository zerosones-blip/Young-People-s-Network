from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.notification = Notification.objects.create(user=self.user, message='Test notification.')

    def test_notification_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('notifications:notification_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test notification.')
