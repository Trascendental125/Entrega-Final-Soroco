from django.shortcuts import render

# Create your views here.

from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClienteForm

# Create your views here.
from .models import Cliente


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "Cliente/index.html", contexto)


# def crear_clientes(request):
#     from datetime import date
#     return redirect("cliente:home")


def crear_cliente(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clientes:home")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "Clientes/crear.html", {"form": form})
