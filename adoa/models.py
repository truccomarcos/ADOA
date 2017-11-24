from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import *
from ckeditor.fields import RichTextField


# Create your models here.
class Patron(models.Model):
    titulo = RichTextField()
    descripcion = RichTextField()
    problemas = RichTextField()
    solucion = RichTextField()
    def __unicode__(self):
       return self.titulo

class ContenidoPatron(models.Model):
    orden = models.IntegerField()
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)
    def _get_titulo(self):
        return self.titulo
    def _get_descripcion(self):
        return self.descripcion
    def _get_orden(self):
        return self.orden
    def __unicode__(self):
       return self.titulo

class ObjetoAprendizaje(models.Model):
    titulo = RichTextField()
    descripcion = RichTextField()
    patron = models.ForeignKey(Patron)
    user = models.ForeignKey(User)
    contenidos = models.OneTom
    # setearContenidos()
    # setearActividad()
    def setearContenidos(self):
        li=[]
        for contenido in self.patron.contenidopatron_set.all():
            li.append(Contenido(titulo = contenido._get_titulo(), descripcion = contenido._get_descripcion(), orden = contenido._get_orden(),objetoAprendizaje = self))
        # for contenidoPatron in ContenidoPatron.objects.all():
        #     if contenidoPatron.patron == self.patron:
        #         contenido = Contenido(titulo = contenidoPatron._get_titulo(), descripcion = contenidoPatron._get_descripcion(), orden = contenidoPatron._get_orden(),objetoAprendizaje = self)
        #         li.append(contenido)
        return li
    def setearActividad(self,bulk=False):
        li=[]
        vof=VerdaderoFalso(titulo = "VerdaderoFalso", descripcion = "aoifjoiajs", enunGeneral = "oiafsoij", objetoAprendizaje= self)
        li.append(vof)
        return li
    def __unicode__(self):
       return self.titulo

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
    titulo = RichTextField()
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo

#--------------------------------------------------------------------------

class VerdaderoFalso(Actividad):
    enunGeneral =  RichTextField()
    descripcion = RichTextField()


class ElementoVoF(models.Model):
    enunciado = RichTextField()
    verdad = models.BooleanField()
    VoF = models.ForeignKey(VerdaderoFalso)

#--------------------------------------------------------------------------

class Ordenamiento(Actividad):
    enunGeneral =  RichTextField()
    descripcion = RichTextField()

class ElementoOrdenamiento(models.Model):
    enunciado = RichTextField()
    orden = models.IntegerField()
    ordenamiento = models.ForeignKey(Ordenamiento)

#--------------------------------------------------------------------------
class OpcionMultiple(Actividad):
    enunGeneral = RichTextField()
    descripcion = RichTextField()

class ElementoOpcionMultiple(models.Model):
    enunciado = RichTextField()
    correcta = RichTextField()
    incorrecta1 = RichTextField()
    incorrecta2 = RichTextField()
    incorrecta3 = RichTextField()
    multiple = models.ForeignKey(OpcionMultiple)

#-------------------------------------------------------------

class Identificacion(Actividad):
    enunGeneral = RichTextField()
    descripcion = RichTextField()

class ElementoIdentificacion(models.Model):
    enunciado = RichTextField()
    correcto = models.BooleanField()
    identificacion = models.ForeignKey(Identificacion)

#----------------------------------------------------------

class Asociacion(Actividad):
    enunGeneral = RichTextField()
    descripcion = RichTextField()

class ElementoAsosiacion(models.Model):
    enunciado = RichTextField()
    imagen = models.ImageField()
    asociacion = models.ForeignKey(Asociacion)
