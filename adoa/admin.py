# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Patron)
admin.site.register(ContenidoPatron)
admin.site.register(ObjetoAprendizaje)
admin.site.register(Contenido)
admin.site.register(ElementoVoF)
admin.site.register(ElementoOrdenamiento)
admin.site.register(ElementoOpcionMultiple)
admin.site.register(ElementoIdentificacion)
admin.site.register(ElementoAsociacion)
