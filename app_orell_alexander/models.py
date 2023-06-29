
from django.db import models

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="productos",null=True)
