from rest_framework import serializers
from rest_framework.response import Response
from .models import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarefaModel
        fields = [
            "id",
            "nome",
            "decricao",
            "feito",
            "delete",
            "user"
        ]
    
    def create(self,validated_data):
        return super().create(validated_data)