from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

from . import forms


def home(request):
    return render(request, "Home/index.html")

# Login
def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "Home/login.html", {"form": form})

# Vista para el registro
def register(request):
    # Aquí debes implementar la lógica para el registro de usuarios
    # Por ejemplo, crear un nuevo usuario con el formulario de registro
    # y realizar acciones adicionales necesarias.
    return render(request, "Home/register.html")

