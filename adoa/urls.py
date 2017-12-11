from django.conf.urls import include, url
from adoa.views import *

# from . import views

urlpatterns = [
    # url(r'^$', index, name='index'),
    url(r'^$', Index.as_view()),
    url(r'^index/', Index.as_view(), name='index'),


    url(r'^queEsOA/', QueEsOA.as_view(), name='queEsOA'),
    url(r'^queEsPatron/', QueEsPatron.as_view(), name='queEsPatron'),
    url(r'^ayuda/', Ayuda.as_view(), name='ayuda'),
    url(r'^patrones/', PatronesView.as_view(), name = 'patrones'),

    url(r'^oa/$', ObjetoAprendizajeList.as_view(), name='list'),
    url(r'^oa/(?P<pk>\d+)$', ObjetoAprendizajeDetail.as_view(), name='detail'),
    url(r'^oa/nuevo$', ObjetoAprendizajeCreate.as_view(), name='new'),
    url(r'^oa/editar/(?P<pk>\d+)$', ObjetoAprendizajeUpdate.as_view(), name='edit'),
    url(r'^oa/borrar/(?P<pk>\d+)$', ObjetoAprendizajeDelete.as_view(), name='delete'),
    url(r'^oa/patron$', ContenidoView.as_view(), name='patron'),
    url(r'^oa/contenido$', ContenidoCreate.as_view(), name='contenido'),
    url(r'^oa/elementoasociacion$', ElementoAsociacionCreate.as_view(), name='elementoasociacion'),
    url(r'^oa/elementovof$', ElementoVoFCreate.as_view(), name='elementovof'),
    url(r'^oa/elementoidentificacion$', ElementoIdentificacionCreate.as_view(), name='elementoidentificacion'),
    url(r'^oa/elementoordenamiento$', ElementoOrdenamientoCreate.as_view(), name='elementoordenamiento'),
    url(r'^oa/elementoopcionmultiple$', ElementoOpcionMultipleCreate.as_view(), name='elementoopcionmultiple'),



    # url(r'^oa/actividad$', ActividadCreate.as_view(), name='actividad'),

    # url(r'^oa/contenidos/(?P<pk>\d+)$', ActividadCreate.as_view(), name='contenidos'),

    # url(r'^OA/', ListOAView.as_view(), name='oa_list'),
    # url(r'^OA/new/$', OAFormView.as_view(), name='oa_new'),
    # url(r'^OA/new/contenidos/$', CreateOAView.as_view(), name='oa_contenidos'),
    # url(r'^OA/new/actividades/$', OAActividadesFormView.as_view(), name='oa_actividades'),
    # url(r'^OA/new/final/$', OAFinalView.as_view(), name='oa_final'),
]
    # url(r'^inicioOA/', inicioOA, name = 'inicioOA'),
    # url(r'^contenidosOA/', contenidosOA, name = 'contenidosOA'),
    # url(r'^OA/(?P<oa_id>[0-9]+)/$', detail, name='detail'),
    # url(r'^OA/(?P<oa_id>[0-9]+)/edit$', edit, name='edit'),

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
