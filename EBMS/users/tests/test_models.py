from django.test import TestCase
from ..models import User
from django.core.exceptions import ValidationError

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email = 'user@test.com', password = 'testpassword')
        self.superuser = User.objects.create_superuser(email = 'admin@test.com',
                                                       password = 'testpassword'
                                                       )

    def test_create_user(self):
        self.assertEqual(self.user.email, 'user@test.com')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(self.superuser.email, 'admin@test.com')
        self.assertTrue(self.superuser.check_password('testpassword'))
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)
    
    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email = None, password = 'testpassword')

    def test_create_superuser_without_is_staff(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email = 'a@a.a', password = 'p', is_staff = False)

    def test_create_superuser_without_is_superuser(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email = 'a@a.a', password = 'p', is_superuser = False)

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'user@test.com')

    def test_user_verbose_name_plural(self):
        self.assertEqual(str(User._meta.verbose_name_plural), 'Users')