from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        ''' Converts password from str to hashed value '''
        return make_password(value, hasher='default')

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password', 'is_active')

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['username'],
                password=validated_data['password'],
                is_active=validated_data['is_active'],)
            return user
