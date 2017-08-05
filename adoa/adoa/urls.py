from django.conf.urls import *
from adoa.views import *
from django.conf.urls import include, url
	


urlpatterns = [

    url(r'^$', index),
    url(r'^index/', index, name='index'),
    url(r'^ayuda/', ayuda, name='ayuda'),
    url(r'^queEsOA/', queEsOA, name='queEsOA'),
    url(r'^queEsPatron/', queEsPatron, name='queEsPatron'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^inicioOA/', inicioOA, name = 'inicioOA'),
    url(r'^contenidosOA/', contenidosOA, name = 'contenidosOA'),
    url(r'^guardarcontenidosOA/', guardarcontenidosOA, name = 'guardarcontenidosOA'),
    url(r'^guardarActividadesOA/', guardarActividadesOA, name = 'guardarActividadesOA'),    
    url(r'^patrones/', patrones, name = 'patrones'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),



]

