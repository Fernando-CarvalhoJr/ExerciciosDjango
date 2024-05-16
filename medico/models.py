from django.db import models

# Create your models here.
from django.db import models

class medico(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField()
    crm = models.IntegerField(max_length=6)
    especialidade_id = models.IntegerField()


class especialidade(models.Model):
    nome = models.CharField(max_length=30)
    descrição = models.CharField(max_length=300)