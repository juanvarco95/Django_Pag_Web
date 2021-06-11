from django.db import models
from django.db.models.fields import TextField

class Servicio(models.Model):
    titulo = models.CharField(max_length = 50, verbose_name = "Título")
    contenido = models.CharField(max_length = 300)
    imagen = models.ImageField(upload_to = 'servicios' ,verbose_name = "Imágen")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
