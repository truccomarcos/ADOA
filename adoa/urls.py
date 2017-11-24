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
    url(r'^contenidosOA/', contenidosOA, name = 'contenidosOA'),
    url(r'^OA/(?P<oa_id>[0-9]+)/$', detail, name='detail'),
    url(r'^OA/(?P<oa_id>[0-9]+)/edit$', edit, name='edit'),

    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # ex: /polls/5/results/
    # url(r'^(?P<oa_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<oa_id>[0-9]+)/vote/$', views.vote, name='vote'),



    # url(r'^contenidosOA/', contenidosOA, name = 'contenidosOA'),
    # url(r'^guardarcontenidosOA/', guardarcontenidosOA, name = 'guardarcontenidosOA'),
    # url(r'^guardarActividadesOA/', guardarActividadesOA, name = 'guardarActividadesOA'),
    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	# url(r'^admin/', include(admin.site.urls)),
]
