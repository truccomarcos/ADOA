# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Patron)
admin.site.register(ContenidoPatron)
admin.site.register(ObjetoAprendizaje)
admin.site.register(Contenido)
admin.site.register(Actividad)
admin.site.register(VerdaderoFalso)
admin.site.register(ElementoVoF)
admin.site.register(Ordenamiento)
admin.site.register(ElementoOrdenamiento)
admin.site.register(OpcionMultiple)
admin.site.register(ElementoOpcionMultiple)
admin.site.register(Identificacion)
admin.site.register(ElementoIdentificacion)
admin.site.register(Asociacion)
admin.site.register(ElementoAsosiacion)
