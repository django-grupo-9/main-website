from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm


def index(request):
    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def docentes(request):
    return render(request, "pages/docentes.html", {"title": "DOCENTES"})


def contacto(request):    
    return render(request, 'pages/contacto.html', {"title": "CONTACTO"})


def sign(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form2 = SignUpForm(request.POST)
    else:
        form = LoginForm()
        form2 = SignUpForm()
    return render(request, 'pages/sign.html', {"title": "Ingresar", 'form': form, 'form2': form2})
