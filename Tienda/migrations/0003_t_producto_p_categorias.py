# Generated by Django 3.2.2 on 2021-06-12 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tienda', '0002_auto_20210612_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_producto',
            name='p_categorias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]