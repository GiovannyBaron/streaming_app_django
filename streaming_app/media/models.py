from django.db import models
from user.models import User


class MediaCatalog(models.Model):
    GENDER_CHOICES = [
        ('fantasia', 'Fantasia'), ('accion', 'Accion'),
        ('comedia', 'Comedia'), ('terror', 'Terror'),
        ('drama', 'Drama'), ('infantil', 'Infantil')]
    TYPE_CHOICES = [('pelicula', 'Pelicula'), ('serie', 'Serie')]

    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=255, choices=GENDER_CHOICES)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.nombre
    

class MediaUsuarios(models.Model):
    media = models.ForeignKey(MediaCatalog, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.FloatField(null=True)

    def __str__(self):
        return self.media


class MediaUsuariosCount(models.Model):
    media = models.ForeignKey(MediaCatalog, on_delete=models.CASCADE)
    num_usuarios = models.IntegerField()
    avg_score = models.FloatField(null=True)

    def __str__(self):
        return self.media


