from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    cuit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"