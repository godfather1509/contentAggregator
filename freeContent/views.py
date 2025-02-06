from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from .serializer import RegisterUser,LoginSerializer
from .models import UserRegistration
from rest_framework_simplejwt.tokens import RefreshToken

class Register(ModelViewSet):
    serializer_class=RegisterUser
    queryset=UserRegistration.objects.all()
# Create your views here.

class Login(APIView):

    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if serializer.is_valid():
            email=serializer.data["email"]
            password=serializer.data["password"]
            user=UserRegistration.objects.get(email=email)
            if user is None or user.password!=password:
                return Response({
                    'message':"Invalid Credentials",
                    'data':{}})
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),})

        return Response({'data':serializer.errors})
