# Generated by Django 3.2.2 on 2021-06-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0014_t_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]