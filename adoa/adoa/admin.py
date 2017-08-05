from django.contrib import admin
from adoa.models import *
from forms import *


class ObjetoAprendizajeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion','patron','user')


class PatronAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'problemas', 'solucion')



class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido','objetoAprendizaje')


class VerdaderoFalsoAdmin(admin.ModelAdmin):
    list_display = ('enunGeneral', 'descripcion')


class OrdenamientoAdmin(admin.ModelAdmin):
    list_display = ('enunGeneral', 'descripcion')


class ElementoOrdenamientoAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'orden')


class ElementoVoFAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'verdad')


class OpcionMultipleAdmin(admin.ModelAdmin):
    list_display = ('enunGeneral', 'descripcion')


class ElementoOpcionMultipleAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'correcta', 'incorrecta1', 'incorrecta2',
         'incorrecta3')

class ContenidoPatronAdmin(admin.ModelAdmin):
    list_display = ('orden', 'patron','titulo')

    

admin.site.register(ObjetoAprendizaje, ObjetoAprendizajeAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(VerdaderoFalso, VerdaderoFalsoAdmin)
admin.site.register(ElementoVoF, ElementoVoFAdmin)
admin.site.register(ElementoOrdenamiento, ElementoOrdenamientoAdmin)
admin.site.register(OpcionMultiple, OpcionMultipleAdmin)
admin.site.register(ElementoOpcionMultiple, ElementoOpcionMultipleAdmin)
admin.site.register(ContenidoPatron, ContenidoPatronAdmin)