from django.test import TestCase
from django.urls import resolve
from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, WhoAmIView, LoginAPIView, LogoutAPIView

class URLTest(TestCase):
    def test_user_list_create_api_view_url(self):
        resolver = resolve('/users/')
        self.assertEqual(resolver.func.view_class, UserListCreateAPIView)

    def test_user_retrieve_update_destroy_api_view_url(self):
        resolver = resolve('/users/1/')
        self.assertEqual(resolver.func.view_class, UserRetrieveUpdateDestroyAPIView)

    def test_who_am_i_view_url(self):
        resolver = resolve('/whoami/')
        self.assertEqual(resolver.func.view_class, WhoAmIView)

    def test_login_api_view_url(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.func.view_class, LoginAPIView)

    def test_logout_api_view_url(self):
        resolver = resolve('/logout/')
        self.assertEqual(resolver.func.view_class, LogoutAPIView)