# Generated by Django 3.2.2 on 2021-06-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0013_auto_20210613_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
