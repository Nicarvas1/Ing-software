from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DocumentForm  # Asegúrate de importar DocumentForm desde forms.py
from .models import Documentos  # Importa tu modelo Documentos
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Comment
from .forms import CommentForm  # Asegúrate de crear un formulario de comentarios
from .forms import *
from .forms import DocumentForm
from .models import Documentos

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

@login_required
def document_list(request):
    documents = Documentos.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

@staff_member_required
def subir_casos(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_caso = form.save()
            return HttpResponseRedirect('/')  # Redirige a donde quieras después de guardar
    else:
        form = DocumentForm()
    
    return render(request, 'core/subida_casos.html', {'form': form})
# cometarios
def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form' :registro})
@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')  # Redirige a la lista de comentarios
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

@login_required
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

@staff_member_required
def comment_edit(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_edit.html', {'form': form})

@staff_member_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request, 'comment_delete.html', {'comment': comment})



def search_documents(request):
    query = request.GET.get('q')
    if query:
        documents = Documentos.objects.filter(name__icontains=query)
    else:
        documents = Documentos.objects.all()
    return render(request, 'document_list.html', {'documents': documents})
