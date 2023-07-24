from typing import Any
from django.contrib.auth.decorators import login_required

# importaciones para login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# PAGINA PRINCIPAL


@login_required
def index(request):
    return render(request, "Seguros/index.html")

class SeguroCategoriaList(ListView):
    model = models.SeguroCategoria


class SeguroCategoriaCreate(CreateView):
    model = models.SeguroCategoria
    form_class = forms.SeguroCategoriaForm
    success_url = reverse_lazy("Seguros:segurocategoria_list")


class SeguroCategoriaDetail(DetailView):
    model = models.SeguroCategoria


class SeguroCategoriaUpdate(UpdateView):
    model = models.SeguroCategoria
    form_class = forms.SeguroCategoriaForm
    success_url = reverse_lazy("Seguros:segurocategoria_list")


class SeguroCategoriaDelete(DeleteView):
    model = models.SeguroCategoria
    success_url = reverse_lazy("Seguros:segurocategoria_list")


class SeguroList(ListView):
    model = models.Seguro

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Seguro.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Seguro.objects.all()
        return object_list


class SeguroCreate(CreateView):
    model = models.Seguro
    form_class = forms.SeguroForm
    success_url = reverse_lazy("producto:producto_list")


class SeguroDetail(DetailView):
    model = models.Seguro


class SeguroUpdate(UpdateView):
    model = models.Seguro
    form_class = forms.SeguroForm
    success_url = reverse_lazy("Seguros:seguro_list")


class SeguroDelete(DeleteView):
    model = models.Seguro
    success_url = reverse_lazy("Seguros:seguro_list")