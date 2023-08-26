from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class CustomTokenObtainParirSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
            if user.suspenso:
                raise AuthenticationFailed("Conta está suspensa")
            
            token = super().get_token(user)
            token['user_id'] = str(user.id)
            token['username']= user.username
            token['email']=user.email
            token['tipo']= user.tipo
            token['suspenso'] = user.suspenso

            return token
                
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True)
    token = serializers.SerializerMethodField()
    
    class Meta:
        model=UserModel
        fields=[
            'id',
            'username',
            'email',
            'password',
            'tipo',
            'suspenso',
            'token'
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
        validated_data['tipo'] ='client'

        user = super().create(validated_data)
        user.token = self.get_tokens(user)
        return user
    

class UserListSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = UserModel
          fields=["id",
                  'username','email','tipo','suspenso']
          
