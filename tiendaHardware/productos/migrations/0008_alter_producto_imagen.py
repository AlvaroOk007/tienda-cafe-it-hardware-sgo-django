# Generated by Django 5.1.1 on 2024-10-01 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_categoria_alter_producto_imagen_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos/'),
        ),
    ]
