# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass123'))

class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='password123')

    def test_profile_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/account/profile/')

    def test_profile_view_logged_in(self):
        self.client.login(username='john', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'john')

    def test_edit_profile_post(self):
        self.client.login(username='john', password='password123')
        response = self.client.post(reverse('edit_profile'), {
            'username': 'johnny',
            'email': 'john@example.com'
        })
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'johnny')
