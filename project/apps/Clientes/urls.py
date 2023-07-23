from django.urls import path

from .views import crear_cliente, home #busqueda

app_name = "Clientes"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_cliente, name="crear"),
    #path('busqueda/', busqueda, name="busqueda")
]