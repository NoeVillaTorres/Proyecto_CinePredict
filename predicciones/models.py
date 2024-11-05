from django.db import models

from cines.models import Cine

class Prediccion(models.Model):
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE, related_name="predicciones")
    pelicula = models.CharField(max_length=200)
    fecha_prediccion = models.DateTimeField(auto_now_add=True)
    exito_probable = models.FloatField()

    def __str__(self):
        return f"{self.pelicula} - {self.cine.nombre}"