from rest_framework import serializers
from .models import UserRegistration
from rest_framework.serializers import ModelSerializer
from .models import UserRegistration

class RegisterUser(ModelSerializer):
    class Meta:
        model=UserRegistration
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()