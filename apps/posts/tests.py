from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment, Tag, PostView

User = get_user_model()

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.post = Post.objects.create(author=self.user, content='This is a test post.')

    def test_post_creation(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.content, 'This is a test post.')

    def test_post_detail_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('posts:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('posts:post_create'), {
            'content': 'New post content.',
            'image': None
        })
        new_post = Post.objects.get(content='New post content.')
        self.assertEqual(new_post.author.username, 'testuser')

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.post = Post.objects.create(author=self.user, content='This is a test post.')
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='This is a test comment.')

    def test_comment_creation(self):
        self.assertEqual(self.comment.author.username, 'testuser')
        self.assertEqual(self.comment.content, 'This is a test comment.')

    def test_comment_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('posts:comment_create', kwargs={'pk': self.post.pk}), {
            'content': 'New comment content.'
        })
        new_comment = Comment.objects.get(content='New comment content.')
        self.assertEqual(new_comment.author.username, 'testuser')
