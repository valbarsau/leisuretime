from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return self.nombre
    
class Editorial(models.Model):
    nombre=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return self.nombre
    
class Genero(models.Model):
    categoria=models.CharField(max_length=20)
    def __unicode__(self):
        return self.categoria
    
class Usuario(User):
    id_usuario= models.IntegerField(unique=True)
    localizacion=models.TextField()
    def __unicode__(self):
        return self.username
    

class Libro(models.Model):
    isbn=models.CharField(max_length=20)
    titulo=models.CharField(max_length=20)
    descripcion=TextField(blank=True)
    autor=models.ForeignKey(Autor)
    anyo=models.IntegerField()
    generos=models.ManyToManyField(Genero)
    editorial=models.ForeignKey(Editorial)
    usuarios=models.ManyToManyField(Usuario,through="Puntuacion")
    
    def __unicode__(self):
        return self.titulo
    
class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario)
    libro = models.ForeignKey(Libro)
    puntuacion = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    def __unicode__(self):
        return str(self.puntuacion)
