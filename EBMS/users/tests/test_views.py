from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from ..models import User

class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@test.com', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_user_list_create_api_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, HTTP_200_OK)

        data = {
            'email': 'newuser@test.com', 
            'password': 'password',
            'first_name': 'First',
            'last_name': 'Last',
            'title': 'MR',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }
        response = self.client.post(reverse('users'), data=data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_user_retrieve_update_destroy_api_view(self):
        response = self.client.get(reverse('user', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_who_am_i_view(self):
        response = self.client.get(reverse('whoami'))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_login_api_view(self):
        # Test with valid credentials
        data = {'email': 'testuser@test.com', 'password': 'password'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

        # Test with invalid email
        data = {'email': 'wronguser@test.com', 'password': 'password'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

        # Test with invalid password
        data = {'email': 'testuser@test.com', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_logout_api_view(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, HTTP_200_OK)