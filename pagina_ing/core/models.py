from django.db import models

# Create your models here.
class Documentos(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre_caso = models.CharField(max_length=250)
    archivo = models.FileField(upload_to='documentos/')