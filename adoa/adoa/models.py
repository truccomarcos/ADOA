from django.db import models
from django.contrib import admin
# from tinymce.models import HTMLField
from django.contrib.auth.models import *
from ckeditor.fields import RichTextField
# Create your models here.



class Patron(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = RichTextField()
    problemas = RichTextField()
    solucion = RichTextField()
    def __unicode__(self):
       return self.titulo


class ContenidoPatron(models.Model):
    orden = models.IntegerField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length = 200)
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
    titulo=models.CharField(max_length=30)
    descripcion= RichTextField()
    patron = models.ForeignKey(Patron)
    user = models.ForeignKey(User)
    def setearContenidos(self):
        li=[]
        for contenidoPatron in ContenidoPatron.objects.all():
            if contenidoPatron.patron == self.patron:
                contenido = Contenido(titulo = contenidoPatron._get_titulo(), descripcion = contenidoPatron._get_descripcion(), orden = contenidoPatron._get_orden(),objetoAprendizaje = self)
                li.append(contenido)
        return li
    def setearActividad(self):
        li=[]
        vof=VerdaderoFalso(titulo = "VerdaderoFalso", descripcion = "aoifjoiajs", enunGeneral = "oiafsoij", objetoAprendizaje= self)
        li.append(vof)
        return li
    def __unicode__(self):
       return self.titulo


class Contenido(models.Model):
    orden = models.IntegerField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length = 200)
    contenido = RichTextField()
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo

#--------------------------------------------------------------------------

class Actividad(models.Model):
    titulo = models.CharField(max_length=30)
    objetoAprendizaje = models.ForeignKey(ObjetoAprendizaje)
    def __unicode__(self):
       return self.titulo

#--------------------------------------------------------------------------

class VerdaderoFalso(Actividad):
    enunGeneral =  models.CharField(max_length = 30)
    descripcion = RichTextField()


class ElementoVoF(models.Model):
    enunciado = models.CharField(max_length = 30)
    verdad = models.BooleanField()
    VoF = models.ForeignKey(VerdaderoFalso)

#--------------------------------------------------------------------------

class Ordenamiento(Actividad):
    enunGeneral =  models.CharField(max_length = 30)
    descripcion = RichTextField()

class ElementoOrdenamiento(models.Model):
    enunciado = models.CharField(max_length = 30)
    orden = models.IntegerField()
    ordenamiento = models.ForeignKey(Ordenamiento)

#--------------------------------------------------------------------------


class OpcionMultiple(Actividad):
    enunGeneral = models.CharField(max_length = 30)
    descripcion = RichTextField()

class ElementoOpcionMultiple(models.Model):
    enunciado = models.CharField(max_length = 30)
    correcta = models.CharField(max_length = 30)
    incorrecta1 = models.CharField(max_length = 30)
    incorrecta2 = models.CharField(max_length = 30)
    incorrecta3 = models.CharField(max_length = 30)
    multiple = models.ForeignKey(OpcionMultiple)

#-------------------------------------------------------------

class Identificacion(Actividad):
    enunGeneral = models.CharField(max_length = 30)
    descripcion = RichTextField()

class ElementoIdentificacion(models.Model):
    enunciado = models.CharField(max_length = 30)
    correcto = models.BooleanField()
    identificacion = models.ForeignKey(Identificacion)

#----------------------------------------------------------

class Asociacion(Actividad):
    enunGeneral = models.CharField(max_length = 30)
    descripcion = RichTextField()

class ElementoAsosiacion(models.Model):
    enunciado = models.CharField(max_length = 30)
    imagen = models.ImageField()
    asociacion = models.ForeignKey(Asociacion)
