from django.db import models
from usuarios_cine.models import Usuario

class Cine(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cines")

    def __str__(self):
        return self.nombre
