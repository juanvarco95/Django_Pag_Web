from django.db import models
from django.contrib.auth.models import User



class prueba_Categoria(models.Model):
    nombre = models.CharField(max_length = 15)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre

class T_Producto(models.Model):
    nombre = models.CharField(max_length = 15)
    descripcion = models.CharField(max_length = 50, verbose_name = "Descripción")
    imagen = models.ImageField(upload_to = "producto", null = True, blank = True)
    p_categorias = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    pro_categorias =  models.ManyToManyField(prueba_Categoria, verbose_name = "Categorias")
    cantidad = models.IntegerField(null = True) 
    precio = models.DecimalField(max_digits = 8, decimal_places = 3, null = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta: 
        verbose_name = 'producto'
        verbose_name = 'productos'
    
    def __str__(self):
        return self.nombre
        