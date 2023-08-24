from rest_framework import serializers
from user.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True)
    
    class Meta:
        model=UserModel
        fields=[
            'id',
            'username',
            'email',
            'password',
            'tipo',
            'suspenso'
        ]
    
    def create(self,validated_data):
        validated_data['tipo'] ='client'

        user = super().create(validated_data)

        return user
    