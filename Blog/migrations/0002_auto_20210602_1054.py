# Generated by Django 3.2.2 on 2021-06-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=300, verbose_name='Contenido'),
        ),
    ]
