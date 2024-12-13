from django.shortcuts import render, redirect
from .forms import ObraSocialForm, PlanSaludForm, AfiliadoForm

def index(request):
    return render(request, 'ooss/index.html') 

def agregar_obra_social(request):
    if request.method == "POST":
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ObraSocialForm()
    return render(request, 'ooss/agregar_obra_social.html', {'form': form})


def agregar_plan_salud(request):
    if request.method == "POST":
        form = PlanSaludForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlanSaludForm()
    return render(request, 'ooss/agregar_plan_salud.html', {'form': form})


def agregar_afiliado(request):
    if request.method == "POST":
        form = AfiliadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AfiliadoForm()
    return render(request, 'ooss/agregar_afiliado.html', {'form': form})
