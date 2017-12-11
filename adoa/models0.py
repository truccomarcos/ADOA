}from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import *
from ckeditor.fields import RichTextField

ACTIVIDAD_TYPE_CHOICES = (
    ('0', 'VerdaderoFalso'),
    ('1', 'Ordenamiento'),
    ('2', 'OpcionMultiple'),
    ('3', 'Identificacion'),
    ('4', 'Asociacion'),
)
#--------------------------------------------------------------------------
class Patron(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    problemas = RichTextField()
    solucion = RichTextField()
    def get_contenidos(self):
        contenidos = []
        for contenido in self.contenidopatron_set.all():
            contenidos.append(Contenido(titulo = contenido.titulo, descripcion = contenido.descripcion, orden = contenido.orden))
        return contenidos
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class ContenidoPatron(models.Model):
    orden = models.IntegerField()
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    patron = models.ForeignKey(Patron)
#--------------------------------------------------------------------------
class ObjetoAprendizaje(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=140)
    patron = models.ForeignKey(Patron)
    user = models.ForeignKey(User)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class Contenido(models.Model):
    titulo = models.CharField(max_length=30)
    orden = models.CharField(max_length=140)
    descripcion = models.CharField(max_length=500)
    contenido = RichTextField()
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class Actividad(models.Model):
    enunciado = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=ACTIVIDAD_TYPE_CHOICES, null=True)
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class ElementoVoF(models.Model):
    enunciado = models.CharField(max_length=100)
    verdad = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)
#--------------------------------------------------------------------------
class ElementoOrdenamiento(models.Model):
    enunciado = models.CharField(max_length=100)
    orden = models.IntegerField()
    actividad = models.ForeignKey(Actividad, null=True)
#--------------------------------------------------------------------------
class ElementoOpcionMultiple(models.Model):
    enunciado = models.CharField(max_length=100)
    correcta = models.CharField(max_length=100)
    incorrecta1 = models.CharField(max_length=100)
    incorrecta2 = models.CharField(max_length=100)
    incorrecta3 = models.CharField(max_length=100)
    actividad = models.ForeignKey(Actividad, null=True)
#-------------------------------------------------------------
class ElementoIdentificacion(models.Model):
    enunciado = models.CharField(max_length=100)
    correcto = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)
#----------------------------------------------------------
class ElementoAsociacion(models.Model):
    enunciado = models.CharField(max_length=100)
    imagen = models.ImageField()
    actividad = models.ForeignKey(Actividad, null=True)
