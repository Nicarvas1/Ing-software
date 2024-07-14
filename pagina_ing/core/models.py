from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Documentos(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre_caso = models.CharField(max_length=250)
    archivo = models.FileField(upload_to='documentos/')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username}'

    class Meta:
        ordering = ['-created_at']