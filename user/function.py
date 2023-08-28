from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.core.management.base import BaseCommand


                
class UserRoot(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=[
            'id',
            'username',
            'email',
            'password',
            'tipo',
            'suspenso',
           
        ]
    
    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        refresh['user_id'] = str(user.id)
        refresh['username']= user.username
        refresh['email']=user.email
        refresh['tipo']= user.tipo
        refresh['suspenso'] = user.suspenso
       

    def create(self,validated_data):
        validated_data['password'] = make_password(
             validated_data.get("password")
             )
        validated_data['tipo'] ='root'

        user = super().create(validated_data)
        user.token = self.get_tokens(user)
        return user

print("Criar usúarios root")
username = str(input("Digite o username"))
email=str(input("Digite o e-mail"))
password = str(input("Digite o password"))

user = UserRoot(data={"username":username, "email":email, "password":password})

if(user.is_valid()):
    user.save()
    print('User root criado com sucesso!')
else:
    print('Algo deu errado!')
