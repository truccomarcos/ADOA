from __future__ import unicode_literals
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
    titulo = RichTextField()
    descripcion = RichTextField()
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
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)
#--------------------------------------------------------------------------
class ObjetoAprendizaje(models.Model):
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)
    user = models.ForeignKey(User)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class Contenido(models.Model):
    orden = models.IntegerField()
    titulo = RichTextField()
    descripcion = RichTextField()
    contenido = RichTextField()
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class Actividad(models.Model):
    enunciado = RichTextField()
    tipo = models.CharField(max_length=1, choices=ACTIVIDAD_TYPE_CHOICES, null=True)
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo
#--------------------------------------------------------------------------
class ElementoVoF(models.Model):
    enunciado = RichTextField()
    verdad = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)
#--------------------------------------------------------------------------
class ElementoOrdenamiento(models.Model):
    enunciado = RichTextField()
    orden = models.IntegerField()
    actividad = models.ForeignKey(Actividad, null=True)
#--------------------------------------------------------------------------
class ElementoOpcionMultiple(models.Model):
    enunciado = RichTextField()
    correcta = RichTextField()
    incorrecta1 = RichTextField()
    incorrecta2 = RichTextField()
    incorrecta3 = RichTextField()
    actividad = models.ForeignKey(Actividad, null=True)
#-------------------------------------------------------------
class ElementoIdentificacion(models.Model):
    enunciado = RichTextField()
    correcto = models.BooleanField()
    actividad = models.ForeignKey(Actividad, null=True)
#----------------------------------------------------------
class ElementoAsosiacion(models.Model):
    enunciado = RichTextField()
    imagen = models.ImageField()
    actividad = models.ForeignKey(Actividad, null=True)
