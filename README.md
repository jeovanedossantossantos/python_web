# Informações importande 

Obs: para clonar o projeto ```git clone https://github.com/jeovanedossantossantos/python_web.git```


1 - no terminal do vscode novo digite ```python -m venv ""nome da sua venv```

2 - Para ativar a venv digite
    - Linux: ```source env/bin/activate```
    - Windows: ```env\Scripts\activate``` ou ```env\Scripts\activate.bat``` ou ```source venv/Scripts/activate```
    
3 - ```pip install -r ./requirements.txt``` instala todas as dependencias, lembre de antes de executar esse comando criar uma venv para o projeto.

4 - ```python manage.py runserver``` executa a aplicação, abra no link que aparecer no seu terminal

5 - ```python manage.py makemigrations --name user user```

6 - ```python manage.py makemigrations --name tarefa tarefa```

7 - ```python manage.py migrate```

8 - Executa o python shell: ```python manage.py shell```

9 - Importa o UserModel: ```from user.models import UserModel```

10 - Importa o TarefaModel: ```from tarefa.models import TarefaModel```

Criando usuários e tarefas:

11 - ```user = UserModel(username="username", email="email")```

12 - ```user.save()```

13 - ```tarefa = TarefaModel(nome="tarefa",decricao="teste", user_id=user.id)```

14 - ```tarefa.save()```

15 - Buscar todos os usuários: ```users = UserModel.objects.all()```

16 - Pegar todas as tarefas de um user: ```tarefas = TarefaModel.objects.filter(user_id=user.id)```

17 - Sair do python shell: ```exit()```

<a href="https://docs.djangoproject.com/en/4.2/topics/db/models/">Docs Models</a>
<a href="https://docs.djangoproject.com/en/4.2/topics/db/queries/">Making queries</a>
