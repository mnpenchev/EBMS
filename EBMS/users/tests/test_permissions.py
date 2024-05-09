from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from users.permissions import IsSelfOrAdminUser

class IsSelfOrAdminUserTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.permission = IsSelfOrAdminUser()
        self.user = get_user_model().objects.create_user(email='user@test.com', password='password')
        self.admin = get_user_model().objects.create_user(email='admin@test.com', password='password', is_staff=True)

    def test_has_object_permission(self):
        # Test with regular user accessing their own data
        request = self.factory.get('/users/')
        request.user = self.user
        self.assertTrue(self.permission.has_object_permission(request, None, self.user))

        # Test with regular user accessing other user's data
        request = self.factory.get('/users/1/')
        request.user = self.user
        self.assertFalse(self.permission.has_object_permission(request, None, self.admin))

        # Test with admin user accessing other user's data
        request = self.factory.get('/users/1/')
        request.user = self.admin
        self.assertTrue(self.permission.has_object_permission(request, None, self.user))