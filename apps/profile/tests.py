from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Profile, Skill, Experience, Education, SocialLink, Connection, ProfileView

User = get_user_model()

class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.profile = Profile.objects.create(user=self.user, bio='This is a test bio.')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'This is a test bio.')

    def test_profile_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profiles:profile_detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test bio.')

    def test_profile_edit_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('profiles:profile_edit'), {
            'bio': 'Updated bio.'
        })
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio.')
