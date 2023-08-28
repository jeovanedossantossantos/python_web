from django.shortcuts import render

from .serializers import UserSerializer, CustomTokenObtainParirSerializer
from rest_framework import generics
from .models import UserModel

from rest_framework_simplejwt.views import TokenObtainPairView

class CreateUserView(generics.CreateAPIView):
    
    model=UserModel

    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainParirSerializer