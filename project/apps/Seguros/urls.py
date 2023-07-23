from django.urls import path

from . import views

app_name = "Seguros"

urlpatterns = [path("", views.index, name="home")]

# SEGUROCATEGORIA
urlpatterns += [
    path("segurocategoria/list/", views.SeguroCategoriaList.as_view(), name="segurocategoria_list"),
    path("segurocategoria/create/", views.SeguroCategoriaCreate.as_view(), name="segurocategoria_create"),
    path("segurocategoria/detail/<int:pk>", views.SeguroCategoriaDetail.as_view(), name="segurocategoria_detail"),
    path("segurocategoria/update/<int:pk>", views.SeguroCategoriaUpdate.as_view(), name="segurocategoria_update"),
    path("segurocategoria/delete/<int:pk>", views.SeguroCategoriaDelete.as_view(), name="seguroategoria_delete"),
]

# SEGURO
urlpatterns += [
    path("seguro/list/", views.SeguroList.as_view(), name="seguro_list"),
    path("seguro/create/", views.SeguroCreate.as_view(), name="seguro_create"),
    path("seguro/detail/<int:pk>", views.SeguroDetail.as_view(), name="seguro_detail"),
    path("seguro/update/<int:pk>", views.SeguroUpdate.as_view(), name="seguro_update"),
    path("seguro/delete/<int:pk>", views.SeguroDelete.as_view(), name="seguro_delete"),
]