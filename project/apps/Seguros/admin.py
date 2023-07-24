from django.contrib import admin
from . import models

admin.site.site_title = "Seguros"




@admin.register(models.SeguroCategoria)
class SeguroCategoriaAdmin(admin.ModelAdmin):
    list_display = ("riesgo", "descripcion")
    list_filter = ("riesgo",)
    search_fields = ("riesgo", "descripcion")
    ordering = ("riesgo",)


@admin.register(models.Seguro)
class SeguroAdmin(admin.ModelAdmin):
    list_display = (
        "riesgo",
        "seccion",
        "descripcion",
        "suma",
        "fecha_suscripcion",

    )
    list_display_links = ("riesgo",)
    search_fields = ("riesgo",)
    ordering = (
        "descripcion",
        "riesgo"
    )
    list_filter = ("descripcion",)
    date_hierarchy = "fecha_suscripcion"