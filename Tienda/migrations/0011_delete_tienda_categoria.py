# Generated by Django 3.2.2 on 2021-06-12 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0010_alter_t_producto_categorias'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tienda_Categoria',
        ),
    ]
