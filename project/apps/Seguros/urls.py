from django.urls import path

from . import views

app_name = "Seguros"

urlpatterns = [path("", views.index, name="home")]

# SEGUROCATEGORIA
urlpatterns += [
    path("seguroscategoria/list/", views.SegurosCategoriaList.as_view(), name="seguroscategoria_list"),
    path("seguroscategoria/create/", views.SegurosCategoriaCreate.as_view(), name="seguroscategoria_create"),
    path("seguroscategoria/detail/<int:pk>", views.SegurosCategoriaDetail.as_view(), name="seguroscategoria_detail"),
    path("seguroscategoria/update/<int:pk>", views.SegurosCategoriaUpdate.as_view(), name="seguroscategoria_update"),
    path("seguroscategoria/delete/<int:pk>", views.SegurosCategoriaDelete.as_view(), name="seguroscategoria_delete"),
]

# SEGURO
urlpatterns += [
    path("seguros/list/", views.SegurosList.as_view(), name="seguros_list"),
    path("seguros/create/", views.SegurosCreate.as_view(), name="seguros_create"),
    path("seguros/detail/<int:pk>", views.SegurosDetail.as_view(), name="seguros_detail"),
    path("seguros/update/<int:pk>", views.SegurosUpdate.as_view(), name="seguros_update"),
    path("seguros/delete/<int:pk>", views.SegurosDelete.as_view(), name="seguros_delete"),
]