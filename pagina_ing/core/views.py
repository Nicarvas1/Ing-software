from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DocumentForm  # Asegúrate de importar DocumentForm desde forms.py
from .models import Documentos  # Importa tu modelo Documentos

def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def subida_casos(request):
    return render(request, 'core/subida_casos.html')

def about(request):
    return render(request, 'core/about.html')

def advisor(request):
    return render(request, 'core/advisor.html')

def blog(request):
    return render(request, 'core/blog.html')

def contact(request):
    return render(request, 'core/contact.html')

def feature(request):
    return render(request, 'core/feature.html')

def review(request):
    return render(request, 'core/review.html')

def service(request):
    return render(request, 'core/service.html')

def single(request):
    return render(request, 'core/single.html')

def subir_casos(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_caso = form.save()
            return HttpResponseRedirect('/')  # Redirige a donde quieras después de guardar
    else:
        form = DocumentForm()
    
    return render(request, 'core/subida_casos.html', {'form': form})