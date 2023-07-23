from django.contrib import admin

from . import models

admin.site.site_title = "Seguros"

# admin.site.register(models.ProductoCategoria)


@admin.register(models.SeguroCategoria)
class SeguroCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


@admin.register(models.Seguro)
class SeguroAdmin(admin.ModelAdmin):
    list_display = (
        "categoria",
        "nombre",
        "unidad_de_medida",
        "cantidad",
        "precio",
        "descripcion",
        "fecha_actualizacion"
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre"
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"