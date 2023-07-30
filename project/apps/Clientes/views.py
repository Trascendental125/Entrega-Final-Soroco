from django.shortcuts import render

# Create your views here.

from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClientesForm

# Create your views here.
from .models import Clientes


def home(request):
    clientes_registros = Clientes.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "Cliente/index.html", contexto)


# def crear_clientes(request):
#     from datetime import date
#     return redirect("cliente:home")


def crear_cliente(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clientes:home")
    else:  # request.method == "GET"
        form = ClientesForm()
    return render(request, "Clientes/crear.html", {"form": form})
