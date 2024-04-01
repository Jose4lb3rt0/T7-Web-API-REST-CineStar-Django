from django.db import models

# Create your models here.

class Cine(models.Model):
    id = models.AutoField(primary_key=True)
    RazonSocial = models.CharField(max_length=30)
    Salas = models.IntegerField()
    idDistrito = models.IntegerField()
    Direccion = models.CharField(max_length=100)
    Telefonos = models.CharField(max_length=20)

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    fecha_estreno = models.CharField(max_length=10)
    director = models.CharField(max_length=50)
    generos = models.CharField(max_length=10)
    id_clasificacion = models.IntegerField()
    id_estado = models.IntegerField()
    duracion = models.CharField(max_length=3)
    link = models.CharField(max_length=20)
    reparto = models.TextField()
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo