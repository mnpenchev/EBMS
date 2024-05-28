from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
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
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': False, 'default': ''},
            'last_name': {'required': False, 'default': ''},
            'title': {'required': False, 'default': ''},
            'role': {'required': False},
            'is_active': {'required': False},
            'is_staff': {'required': False},
            'is_superuser': {'required': False},
            'groups': {'required': False},
            'user_permissions': {'required': False}
        }
        read_only_fields = ['created']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

