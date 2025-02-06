from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class RegisterUser(ModelSerializer):

    class Meta:
        model =User
        fields=['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is taken')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # `create_user` hashes password automatically
        )
        return user 

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()