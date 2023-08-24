from django.shortcuts import render

from .serializers import UserSerializer
from rest_framework import generics
from .models import UserModel
class CreateUserView(generics.CreateAPIView):
    
    model=UserModel

    serializer_class = UserSerializer
