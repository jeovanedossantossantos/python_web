from django.http import Http404
from django.shortcuts import render
from .middlewares import Middlewares
from .serializers import UserSerializer, CustomTokenObtainParirSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserModel

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        refresh_token=request.data.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'detail':"Logout realizado com sucesso!"},status=200)
            except Exception as e:
                return Response({'detail':"Error ao fazer logout!"},status=400)
        
        return Response({'detail':"O token de autenticação (refresh_token) é necessario para fazer o logout"},status=400)

class CreateUserView(generics.CreateAPIView):
    
    model=UserModel

    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainParirSerializer

class UserViewPrivate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserModel.objects.all()

    def get_queryset(self,pk):
        try:
            return self.queryset.get(pk=pk)
        except UserModel.DoesNotExist:
            raise Http404
    
    def put(self,request, id, format=None):
        user_id = Middlewares.decode(request.headers)
        tipo = self.get_queryset(user_id)
        data = UserSerializer(tipo).data

        if(user_id == id):
            menssagem = 'Changed not passwrod'
            user = self.get_queryset(id)
            userAnt = serializer = UserSerializer(user)
            data = request.data

            try:

                if(user.check_password(data['password_back'])):
                    user.set_password(data['password'])
                    menssagem= "Changed password"
            except:
                menssagem= 'Changed not passwrod'
            
            serializer = UserSerializer(user,data=data)

            if serializer.is_valid():
                serializer.save()

                return Response({
                    "detail": serializer.data, "menssagem":menssagem
                },status=200)
            
            return Response(serializer.error, status=404)
        else:
            return Response({"detail":"Não autorizado!"})


    
