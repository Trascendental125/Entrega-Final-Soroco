from django.db import models
from django.utils import timezone


class SegurosCategoria(models.Model):
    #Categorías de seguros 
    riesgo = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
    max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.riesgo

    class Meta:
        verbose_name = "categoría de seguros"
        verbose_name_plural = "categorías de seguros"


class Seguros(models.Model):
    #Tipos de seguros
    riesgo = models.ForeignKey(SegurosCategoria, on_delete=models.SET_NULL, blank=True, null=True)
    seccion = models.CharField(max_length=250, null=True, blank=True)
    suma = models.FloatField()
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    fecha_suscripcion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de suscripcion")
    foto_inspeccion = models.ImageField(upload_to="fotos_inspeccion", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.riesgo} {self.seccion} {self.descripcion}"