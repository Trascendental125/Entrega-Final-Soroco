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
    return render(request, "seguros/index.html")

class SegurosCategoriaList(ListView):
    model = models.SegurosCategoria


class SegurosCategoriaCreate(CreateView):
    model = models.SegurosCategoria
    form_class = forms.SegurosCategoriaForm
    success_url = reverse_lazy("Seguros:seguroscategoria_list")


class SegurosCategoriaDetail(DetailView):
    model = models.SegurosCategoria


class SegurosCategoriaUpdate(UpdateView):
    model = models.SegurosCategoria
    form_class = forms.SegurosCategoriaForm
    success_url = reverse_lazy("Seguros:seguroscategoria_list")


class SegurosCategoriaDelete(DeleteView):
    model = models.SegurosCategoria
    success_url = reverse_lazy("Seguros:seguroscategoria_list")


class SegurosList(ListView):
    model = models.Seguros

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Seguros.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Seguros.objects.all()
        return object_list


class SegurosCreate(CreateView):
    model = models.Seguros
    form_class = forms.SegurosForm
    success_url = reverse_lazy("Seguros:seguros_list")


class SegurosDetail(DetailView):
    model = models.Seguros


class SegurosUpdate(UpdateView):
    model = models.Seguros
    form_class = forms.SegurosForm
    success_url = reverse_lazy("Seguros:seguros_list")


class SegurosDelete(DeleteView):
    model = models.Seguros
    success_url = reverse_lazy("Seguros:seguros_list")