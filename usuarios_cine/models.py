from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=40, default="N/A")
    apellido_materno = models.CharField(max_length=40, default="N/A")
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# Create your models here.
