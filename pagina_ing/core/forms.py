from django import forms
from .models import Documentos  # Importa tu modelo Documentos

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documentos  # Asegúrate de que coincida con el nombre de tu modelo
        fields = ['codigo', 'nombre_caso', 'archivo']  # Campos del formulario