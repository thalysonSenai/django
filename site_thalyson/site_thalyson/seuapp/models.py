from django.db import models

# Create your models here.
class Usuario(models.Model):
    cpf = models.CharField(max_length=14)
    usuario = models.CharField(max_length=16)
    email = models.CharField(max_length=256)
    nascimento = models.DateField()
    tel = models.CharField(max_length=15)
    senha = models.CharField(max_length=16)

class Agendamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 16)
    sobrenome = models.CharField(max_length = 30)
    celular = models.CharField(max_length = 15)
    data = models.DateField()
    hora = models.TimeField()
