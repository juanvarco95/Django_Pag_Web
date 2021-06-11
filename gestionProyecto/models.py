from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField

class Clientes(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField(blank = True, null = True)
    celular = models.CharField(max_length = 15)

    def __str__(self):
        return self.nombre




