from django.conf.urls import include, url
from adoa.views import *

# from . import views

urlpatterns = [
    # url(r'^$', index, name='index'),
    url(r'^$', index),
    url(r'^index/', index, name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^queEsOA/', queEsOA, name='queEsOA'),
    url(r'^queEsPatron/', queEsPatron, name='queEsPatron'),
    url(r'^ayuda/', ayuda, name='ayuda'),
    url(r'^inicioOA/', inicioOA, name = 'inicioOA'),
    url(r'^patrones/', patrones, name = 'patrones'),

    # url(r'^contenidosOA/', contenidosOA, name = 'contenidosOA'),
    # url(r'^guardarcontenidosOA/', guardarcontenidosOA, name = 'guardarcontenidosOA'),
    # url(r'^guardarActividadesOA/', guardarActividadesOA, name = 'guardarActividadesOA'),
    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	# url(r'^admin/', include(admin.site.urls)),
]
