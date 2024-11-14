from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=30)
    clasificación = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='imagenes_peliculas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
