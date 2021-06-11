from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length = 50, verbose_name = "Título")
    contenido = models.CharField(max_length = 300, verbose_name = "Contenido")
    imagen = models.ImageField(upload_to = "blog", null = True, blank = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categorias = models.ManyToManyField(Categoria, verbose_name = "Categorias")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo



 
