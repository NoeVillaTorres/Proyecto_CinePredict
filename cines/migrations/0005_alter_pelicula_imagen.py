# Generated by Django 5.1.2 on 2024-11-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cines", "0004_alter_pelicula_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pelicula",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="imagenes_peliculas/"
            ),
        ),
    ]
