# Generated by Django 5.1.2 on 2024-11-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cines", "0003_pelicula_delete_cine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pelicula",
            name="imagen",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/imagenes_peliculas/"
            ),
        ),
    ]
