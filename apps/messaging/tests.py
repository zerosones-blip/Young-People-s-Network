from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Conversation, Message

User = get_user_model()

class MessagingTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', email='user1@example.com', password='password')
        self.user2 = User.objects.create_user(username='user2', email='user2@example.com', password='password')
        self.conversation = Conversation.objects.create()
        self.conversation.participants.add(self.user1, self.user2)
        self.message = Message.objects.create(conversation=self.conversation, sender=self.user1, content='Test message.')

    def test_conversation_list_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('messaging:conversation_list'))
        self.assertEqual(response.status_code, 200)

    def test_conversation_detail_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('messaging:conversation_detail', kwargs={'conversation_id': self.conversation.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test message.')

    def test_message_create_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.post(reverse('messaging:message_create', kwargs={'conversation_id': self.conversation.pk}), {
            'content': 'New message content.'
        })
        self.assertEqual(response.status_code, 302)
        new_message = Message.objects.get(content='New message content.')
        self.assertEqual(new_message.sender.username, 'user1')

    def test_message_update_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.post(reverse('messaging:message_update', kwargs={'message_id': self.message.pk}), {
            'content': 'Updated message content.'
        })
        self.assertEqual(response.status_code, 302)
        updated_message = Message.objects.get(pk=self.message.pk)
        self.assertEqual(updated_message.content, 'Updated message content.')

    def test_message_delete_view(self):
        self.client.login(username='user1', password='password')
        response = self.client.post(reverse('messaging:message_delete', kwargs={'message_id': self.message.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Message.DoesNotExist):
            Message.objects.get(pk=self.message.pk)
