# Generated by Django 3.2.2 on 2021-06-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0015_alter_t_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_producto',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
    ]
