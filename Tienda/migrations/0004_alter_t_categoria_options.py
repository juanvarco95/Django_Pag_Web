# Generated by Django 3.2.2 on 2021-06-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_t_producto_p_categorias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_categoria',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
    ]