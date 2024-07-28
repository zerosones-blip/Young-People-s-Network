from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Group

User = get_user_model()

class GroupsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.group = Group.objects.create(name='Test Group', description='This is a test group.')

    def test_group_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('groups:group_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Group')

    def test_group_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('groups:group_detail', kwargs={'group_id': self.group.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test group.')

    def test_group_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('groups:group_create'), {
            'name': 'New Group',
            'description': 'This is a new group.',
        })
        self.assertEqual(response.status_code, 302)
        new_group = Group.objects.get(name='New Group')
        self.assertTrue(self.user in new_group.members.all())

    def test_group_update_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('groups:group_update', kwargs={'group_id': self.group.pk}), {
            'name': 'Updated Group',
            'description': 'This is an updated group.',
        })
        self.assertEqual(response.status_code, 302)
        updated_group = Group.objects.get(pk=self.group.pk)
        self.assertEqual(updated_group.name, 'Updated Group')

    def test_group_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('groups:group_delete', kwargs={'group_id': self.group.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Group.DoesNotExist):
            Group.objects.get(pk=self.group.pk)
