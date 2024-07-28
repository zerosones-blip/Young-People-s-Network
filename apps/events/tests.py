from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Event
from apps.groups.models import Group

User = get_user_model()

class EventsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.group = Group.objects.create(name='Test Group', description='This is a test group.')
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            location='Test Location',
            start_time='2024-07-01T10:00:00Z',
            end_time='2024-07-01T12:00:00Z',
            group=self.group,
            created_by=self.user
        )

    def test_event_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('events:event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('events:event_detail', kwargs={'event_id': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test event.')

    def test_event_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('events:event_create'), {
            'title': 'New Event',
            'description': 'This is a new event.',
            'location': 'New Location',
            'start_time': '2024-07-02T10:00:00Z',
            'end_time': '2024-07-02T12:00:00Z',
            'group': self.group.pk,
        })
        self.assertEqual(response.status_code, 302)
        new_event = Event.objects.get(title='New Event')
        self.assertEqual(new_event.created_by, self.user)

    def test_event_update_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('events:event_update', kwargs={'event_id': self.event.pk}), {
            'title': 'Updated Event',
            'description': 'This is an updated event.',
            'location': 'Updated Location',
            'start_time': '2024-07-01T10:00:00Z',
            'end_time': '2024-07-01T12:00:00Z',
            'group': self.group.pk,
        })
        self.assertEqual(response.status_code, 302)
        updated_event = Event.objects.get(pk=self.event.pk)
        self.assertEqual(updated_event.title, 'Updated Event')

    def test_event_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('events:event_delete', kwargs={'event_id': self.event.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(pk=self.event.pk)
