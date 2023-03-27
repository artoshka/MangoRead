from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser


class RegistrationSerializer(serializers.Serializer):
    profile_img = serializers.ImageField()
    username = serializers.CharField(max_length=10)
    nickname = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    def validate_username(self, username):
        if CustomUser.objects.filter(username=username):
            raise ValidationError("Username is already exist")
        return username


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["profile_img", "email", "username", "nickname", "password"]

