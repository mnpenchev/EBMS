from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'id',
                  'email',
                  'first_name',
                  'last_name',
                  'title',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'created',
                  'updated',
                  'role',
                  'groups',
                  'user_permissions'
                  ]
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['created']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

