from rest_framework.views import APIView
from rest_framework.response import Response
from uuid import UUID
from django.http import Http404
from django.conf import settings
import jwt
from .serializer import TarefaSerializer
from .models import TarefaModel
from user.permissions import ValidToken,IsNotSuspended

class TarefaView(APIView):
    serializer_class = TarefaSerializer
    permission_classes = [ValidToken,IsNotSuspended]
    queryset = TarefaModel.objects.all()

    def get_object(self, pk, user):
        try:
            return self.queryset.get(pk=pk,user=user)
        except TarefaModel.DoesNotExist:
            return Http404
    
    def post(self,request):

        user_id=jwt.decode(request.headers.get('token'), settings.SECRET_KEY,algorithms=["HS256"])
        request.data['user'] = UUID(user_id["user_id"])
        serializer = TarefaSerializer(data=request.data)

        if(serializer.is_valid()):
            tarefa = serializer.save()
            return Response(TarefaSerializer(tarefa).data,status=201)
        
        return Response(serializer.errors, status=400)
    
    def get(self,request,id=None):
        name = request.query_params.get('name')
        user_id=jwt.decode(request.headers.get('token'), 
                           settings.SECRET_KEY,algorithms=["HS256"])
        user = UUID(user_id["user_id"])

        if id is not None:
            tarefa = self.get_object(id,user=user)
            serializer =  TarefaSerializer(tarefa)
        elif name is not None:
            tarefas = self.queryset.filter(nome=name,delete=False,user=user)
            serializer =  TarefaSerializer(tarefas,many=True)
        else:
            tarefas = self.queryset.filter(user=user,delete=False)
            serializer =  TarefaSerializer(tarefas,many=True)
        
        return Response(serializer.data)
    def patch(self,request,id):
        user_id=jwt.decode(request.headers.get('token'), 
                           settings.SECRET_KEY,algorithms=["HS256"])
        user = UUID(user_id["user_id"])
        tarefa = self.queryset.get(id=id,user=user)
        serializer = TarefaSerializer(tarefa,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors,status=400)
    

    def delete(self, request, id):

        user_id=jwt.decode(request.headers.get('token'), 
                           settings.SECRET_KEY,algorithms=["HS256"])
        user = UUID(user_id["user_id"])
        tarefa = self.queryset.get(id=id,user=user)
        tarefa.delete = True
        tarefa.save()

        serializer = TarefaSerializer(tarefa)

        if serializer.data['delete']:
            return Response({"menssage":"Deletado com sucesso!!"},status=200)
        
        return Response({"menssage":"Algo deu errado ao deletar!!"},status=400)
    

