from django.db import models
from uuid import uuid4
from user.models import UserModel
# Create your models here.

class TarefaModel(models.Model):

    id=models.UUIDField(primary_key=True,default=uuid4,editable=False)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="tarefa")
    nome=models.CharField(max_length=150)
    decricao=models.CharField(max_length=254)
    feito = models.BooleanField(default=False)
    delete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


