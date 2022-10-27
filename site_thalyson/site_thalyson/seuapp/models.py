from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    email = models.CharField(max_length=256)
    nascimento = models.DateField()
    tel = models.CharField(max_length=15)
    senha = models.CharField(max_length=16)



