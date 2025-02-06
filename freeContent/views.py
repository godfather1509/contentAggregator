from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from .serializer import RegisterUser,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class Register(ModelViewSet):
    queryset = User.objects.all()  # Add this line
    serializer_class = RegisterUser
    def create(self, request):
        data = request.data 
        serializer = RegisterUser(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            })
        serializer.save()
        return Response({
            'status': True,
            'message': 'User created'
        })        
# Create your views here.

class Login(APIView):

    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if serializer.is_valid():
            email=serializer.data["email"]
            password=serializer.data["password"]
            user=authenticate(email=email,password=password)
            print(email,password)
            if user is None:
                return Response({
                    'message':"Invalid Credentials",
                    'data':{}})
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),})

        return Response({'data':serializer.errors})
