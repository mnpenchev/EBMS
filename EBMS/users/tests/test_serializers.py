from django.test import TestCase
from ..serializers import UserSerializer, LoginSerializer, TokenSerializer
from ..models import User


class TestSerializers(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@test.com',
            'password': 'password',
            'first_name': 'Test',
            'last_name': 'User',
            'title': 'MR',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }
        self.user = User.objects.create_user(**self.user_data)
    
    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        expected_data = {
            'id': self.user.id,
            'email': 'testuser@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'title': 'MR',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }
        serializer_data = serializer.data
        self.assertEqual(serializer_data.get('id'), expected_data.get('id'))
        self.assertEqual(serializer_data.get('email'), expected_data.get('email'))
        self.assertEqual(serializer_data.get('first_name'), expected_data.get('first_name'))
        self.assertEqual(serializer_data.get('last_name'), expected_data.get('last_name'))
        self.assertEqual(serializer_data.get('title'), expected_data.get('title'))
        self.assertEqual(serializer_data.get('is_active'), expected_data.get('is_active'))
        self.assertEqual(serializer_data.get('is_staff'), expected_data.get('is_staff'))
        self.assertEqual(serializer_data.get('is_superuser'), expected_data.get('is_superuser'))


    def test_login_serializer(self):
        data = {'email': 'test@user.com', 'password': 'testpassword'}
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_token_serializer(self):
        data = {'token': 'token'}
        serializer = TokenSerializer(data=data)
        self.assertTrue(serializer.is_valid())
