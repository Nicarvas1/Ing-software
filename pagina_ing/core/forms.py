from django import forms
from .models import Documentos  # Importa tu modelo Documentos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documentos  # Asegúrate de que coincida con el nombre de tu modelo
        fields = ['codigo', 'nombre_caso', 'archivo']  # Campos del formulario
class Registro(UserCreationForm):
    fist_name = forms.CharField(max_length=30, help_text="Ingrese su nombre")
    last_name = forms.CharField(max_length=30, help_text="Ingrese su apellido")
    email = forms.EmailField(max_length=100, help_text="Ingrese su correo")

    class Meta(UserCreationForm.Meta):
        model = User
        filds = ('username', 'first_name', 'last_name','emil','password1','password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']