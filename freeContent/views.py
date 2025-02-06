from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializer import RegisterUser,LoginSerializer



class Register(ModelViewSet):
    queryset = User.objects.all()  # Add this line
    serializer_class = RegisterUser   
# Create your views here.

class Login(APIView):

    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if serializer.is_valid():
            email=serializer.data["email"]
            password=serializer.data["password"]
            user=authenticate(username=serializer.data["username"],password=password)
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "You have access!"})