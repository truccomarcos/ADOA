from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from adoa.models import *
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from forms import *
from django.contrib.sessions import *
from django.contrib.admin import *
from django.forms import formsets
from django.forms import modelformset_factory
from django.forms import formset_factory
from django.forms.models import model_to_dict
import json
import pdb
from bunch import bunchify


# Create your views here.
def index(request):
    context = {
        'title': 'index',
        'form': UserLoginForm(request.POST or None)
    }
    return render(request, 'index.html', context)

def queEsOA():
    context = {
        'title':'Que es un Objeto de Aprendizaje?',
    }
    return render(request, 'queEsOa.html', context)

def queEsPatron():
    context = {
        'title':'Que es un Patron de Aprendizaje?',
    }
    return render(request, 'queEsPatron.html', context)

def ayuda():
    context = {
        'title':'Ayuda',
    }
    return render(request, 'ayuda.html', context)

def oa_new(request):
    form = ObjetoAprendizajeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            oa = form.save(commit=False)
            contenidos = oa.patron.get_contenidos()
            contenidos_serial = []
            for contenido in contenidos:
                contenidos_serial.append(model_to_dict(contenido))
            request.session['oa'] = model_to_dict(oa)
            request.session['contenidos'] = contenidos_serial
            request.method=''
            return oa_contenidos(request)
    else:
        return render (request, 'oa_edit.html', { 'form':form })

def oa_contenidos(request):
    ContenidosObjetoFormset = formset_factory(ContenidoForm, formset=ContenidosFormSet)
    if request.method=='POST':
        contenido_formset = ContenidosObjetoFormset(request.POST)
        if contenido_formset.is_valid():
            contenidos = []
            for contenido_form in contenido_formset:
                contenidos.append(model_to_dict(contenido_form.save(commit=False)))
            request.session['contenidos'] = contenidos
            request.method = ''
            return oa_actividades(request)
        else:
            return render(request, 'error.html')
    else:
        oa = request.session['oa']
        contenidos = request.session['contenidos']
        contenidos_data = [{'orden': int(c['orden']), 'titulo': str(c['titulo']), 'descripcion': str(c['descripcion']), 'contenido': str(c['contenido'])}
                        for c in request.session['contenidos']]
        contenido_formset = ContenidosObjetoFormset(initial = contenidos_data)
        return render(request, 'oa_contenidos.html', { 'oa':oa, 'contenido_formset': contenido_formset })


def oa_actividades(request):
    ActividadesObjetoFormset = formset_factory(ActividadForm, formset=ActividadesFormSet)
    if request.method=='POST':
        actividad_formset = ActividadesObjetoFormset(request.POST)
        if actividad_formset.is_valid():
            actividades = []
            for actividad_form in actividad_formset:
                actividades.append(model_to_dict(actividad_form.save(commit=False)))
            request.session['actividades'] = actividades
            request.method = ''
            return oa_final(request)
        else:
            return render(request, 'error.html')
    else:
        oa = request.session['oa']
        actividad_formset = ActividadesObjetoFormset()
        return render(request, 'oa_actividades.html', { 'oa':oa, 'actividad_formset': actividad_formset })

def oa_final(request):
    if request.method=='POST':
        pdb.set_trace()
        oa = bunchify(request.session['oa'])
        contenidos = bunchify(request.session['contenidos'])
        actividades = bunchify(request.session['actividades'])
        newOa = ObjetoAprendizaje(titulo= oa.titulo, descripcion= oa.descripcion, patron= Patron.objects.get(id=oa.patron), user= User.objects.get(username = request.user))
        newOa.save()
        for contenido in contenidos:
            newOa.contenido_set.create(orden= contenido.orden, titulo= contenido.titulo, descripcion=contenido.descripcion, contenido= contenido.contenido)
        for actividad in actividades:
            newOa.actividad_set.create(titulo= actividad.titulo)
        return render(request, 'oa_final.html', {'oa': oa, 'contenidos': oa.contenido_set, 'actividades': oa.actividad_set})
        # newOa.contenido_set = newContenidos
        # newOa.actividad_set = newActividades
        pdb.set_trace()
    else:
        oa = request.session['oa']
        contenidos = request.session['contenidos']
        actividades = request.session['actividades']
        return render(request, 'save_oa_details.html', {'oa': oa,'contenidos': contenidos, 'actividades':actividades})



    # return render(request, 'error.html')
#
# def inicioOA(request):
#
#     if request.method == 'POST':
#         form = ObjetoAprendizajeForm(request.POST or None)
#         context = {
#
#             'title': 'Inicio OA',
#             'form': form
#         }
#         if form.is_valid():
#             oa = ObjetoAprendizaje(titulo=form.cleaned_data.get("titulo"),descripcion=form.cleaned_data.get("descripcion"), patron=form.cleaned_data.get("patron"),user= User.objects.get(username = request.user))
#             # pdb.set_trace()
#             contenidos = list(oa.setearContenidos())
#             actividades = list(oa.setearActividad())
#             context = {
#                     'oa' : oa,
#                     'contenidos': contenidos,
#                     'actividades': actividades
#                 }
#         # titulo1 = form.cleaned_data.get("titulo")
#         # descripcion1 = form.cleaned_data.get("descripcion")
#         # patron1 = form.cleaned_data.get("patron")
#         # user_request = request.user
#         # user = User.objects.get(username = user_request)
#         # oa = ObjetoAprendizaje(titulo = titulo1, descripcion = descripcion1, patron = patron1, user = user)
#         # if not ObjetoAprendizaje.objects.filter(pk=oa.pk).exists():
#         #     oa.save()
#         #     for contenido in oa.setearContenidos():
#         #         contenido.save()
#         #     for vof in oa.setearActividad():
#         #         print vof
#         #         vof.save()
#         # request.session["oa_pk"] = oa.pk
#
#         # return contenidosOA(request)
#             return contenidosOA(request)
#         else:
#             return render(request,'error.html')
#     else:
#         return render(request, 'inicioOA.html', context)
#
# def contenidosOA(request):
#     title = 'Contenidos OA'
#     # formset = formset_factory(ContenidoForm, extra=oa.contenido_set.count())
#     pdb.set_trace()
#     formset = formset_factory(ContenidoForm, formset=ContenidosFormSet )
#     if request.method == 'POST':
#         lala = 0
#         return render(request, "error.html")
#     else:
#         context = {
#                 "title": title,
#                 "formset": formset,
#         }
#         return render(request,"contenidosOA.html", context)
#     # .set_trace()
#     # for form in oa.contenido_set.all():
#     #     forms.append(ContenidoForm(request.POST or None))
#     # ContenidoFormSet = inlineformset_factory(ObjetoAprendizaje,Contenido,fields=('orden','titulo','descripcion','contenido','objetoAprendizaje'), extra = 0)
#     # formset = ContenidoFormSet(instance = oa)
#     #     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     #     title = 'Contenidos OA'
#     #     ContenidoFormSet =  inlineformset_factory(ObjetoAprendizaje,Contenido,fields=('orden','titulo','descripcion','contenido','objetoAprendizaje'), extra = 0)
#     #     context = {
#     #             "title": title,
#     #         }
#     #
#     #     formset = ContenidoFormSet(instance = oa,)
#     #     context = {
#     #         "title": title,
#     #         "formset": formset,
#     #     }
#     #     return render(request,"contenidosOA.html", context)
#
#
def patrones(request):
    context = {
        'title': 'Patrones',
        'patrones': Patron.objects.all()
    }
    return render(request, 'patrones.html', context)

# def detail(request, oa_id):
#     return HttpResponse("Objeto de Aprendizaje %s." % oa_id)
#
# def edit(request, oa_id):
#     return HttpResponse("Editando Objeto de Aprendizaje %s." % oa_id)

# def archive(request):
#     patrones = Patron.objects.all()
#     mi_template = loader.get_template("archive.html")
#     mi_contexto = Context({'patrones': patrones})
#     return HttpResponse(mi_template.render(mi_contexto))
#
# def ayuda(request):
#     title = 'Sign Up Now'
#     context = {
#         "title": title,
#      }
#     return render (request,"ayuda.html",context)
#
# def queEsOA(request):
#     title = 'Sign Up Now'
#     context = {
#         "title": title,
#      }
#     return render (request,"queEsOA.html",context)
#
# def queEsPatron(request):
#     title = 'Sign Up Now'
#     context = {
#         "title": title,
#      }
#     return render (request,"queEsPatron.html",context)
#
# def index(request):
#     title = 'Sign Up Now'
#     form = UserLoginForm(request.POST or None)
#     context = {
#         "title": title,
#         "form": form
#     }
#     if form.is_valid():
#         instance = form.save(commit=False)
#         username = form.cleaned_data.get("username")
#         if not username:
#             username = "New username"
#         instance.username = username
#         # if not instanc#     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     title = 'Contenidos OA'
#     ContenidoFormSet =  inlineformset_factory(ObjetoAprendizaje,Contenido,fields=('orden','titulo','descripcion','contenido','objetoAprendizaje'), extra = 0)
#     context = {
#             "title": title,
#         }
#
#     formset = ContenidoFormSet(instance = oa,)
#     context = {
#         "title": title,
#         "formset": formset,
#     }
#     return render(request,"contenidosOA.html", context)e.full_name:
#         #    instance.full_name = "Justin"
#         instance.save()
#         context = {
#             "title": "Thank you"
#         }
#     # if request.user.is_authenticated() and request.user.is_staff:
#     #     queryset = User.objects.all()
#     #     context = {
#     #         "queryset": queryset
#     #     }
#     return render(request, "index.html", context)
#
# def inicioOA(request):
#     title = 'Inicio OA'
#     form = ObjetoAprendizajeForm(request.POST or None)
#     context = {
#         "title": title,
#         "form": form
#     }
#     if form.is_valid():
#         titulo1 = form.cleaned_data.get("titulo")
#         descripcion1 = form.cleaned_data.get("descripcion")
#         patron1 = form.cleaned_data.get("patron")
#         user_request = request.user
#         user = User.objects.get(username = user_request)
#         oa = ObjetoAprendizaje(titulo = titulo1, descripcion = descripcion1, patron = patron1, user = user)
#
#         if not ObjetoAprendizaje.objects.filter(pk=oa.pk).exists():
#             oa.save()
#             for contenido in oa.setearContenidos():
#                 contenido.save()
#             for vof in oa.setearActividad():
#                 print vof
#                 vof.save()
#         request.session["oa_pk"] = oa.pk
#
#         context = {
#             "title": "Thank you",
#              "oa": oa
#         }
#
#         return contenidosOA(request)
#     else:
#         return render(request, "inicioOA.html", context)
#
# def contenidosOA(request):
#     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     title = 'Contenidos OA'
#     ContenidoFormSet =  inlineformset_factory(ObjetoAprendizaje,Contenido,fields=('orden','titulo','descripcion','contenido','objetoAprendizaje'), extra = 0)
#     context = {
#             "title": title,
#         }
#
#     formset = ContenidoFormSet(instance = oa,)
#     context = {
#         "title": title,
#         "formset": formset,
#     }
#     return render(request,"contenidosOA.html", context)
#
# def guardarcontenidosOA(request):
#     ContenidoFormSet =  inlineformset_factory(ObjetoAprendizaje,Contenido,fields=('orden','titulo','descripcion','contenido','objetoAprendizaje'), extra = 0)
#     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     formset = ContenidoFormSet(request.POST, instance = oa)
#     title = 'Guardar contenidos OA'
#     context = {
#             "title": title,
#         }
#     for form in formset:
#         print form.as_p
#
#     if formset.is_valid():
#         for f_form in formset:
#             if f_form.is_valid():
#                 orden =  f_form.cleaned_data.get("orden")
#                 titulo = f_form.cleaned_data.get("titulo")
#                 descripcion = f_form.cleaned_data.get("descripcion")
#                 content = f_form.cleaned_data.get("contenido")
#                 objetoAprendizaje = f_form.cleaned_data.get("objetoAprendizaje")
#                 contenido = Contenido(orden = orden, titulo = titulo, descripcion = descripcion,contenido = content, objetoAprendizaje = objetoAprendizaje)
#                 contenido.save()
#             return actividades(request)
#     else:
#         return ayuda(request)
#
# def patrones(request):
#     title = 'Patrones'
#     patrones = Patron.objects.all()
#     form = PatronForm()
#     context = {
#         "title":title,
#         "form": form,
#         "patrones": patrones and request.user.is_staff:
#     #     queryset = User.objects.all()
#     #     context = {
#     #         "queryset": queryset
#     #     }
#     }
#     return render(request,"patrones.html",context)
#
# def actividades(request):
#     title = 'actividades'
#     ActividadFormset = inlineformset_factory(ObjetoAprendizaje,VerdaderoFalso,fields=('titulo','enunGeneral','descripcion','objetoAprendizaje'), extra = 0)
#     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     formset = ActividadFormset(instance = oa)
#     context = {
#         "title": title,
#         "formset": formset,
#     }
#     return render(request,"actividades.html", context)
#
#
# def guardarActividadesOA(request):
#     ActividadFormset = inlineformset_factory(ObjetoAprendizaje,VerdaderoFalso,fields=('titulo','enunGeneral','descripcion','objetoAprendizaje'), extra = 0)
#     oa = ObjetoAprendizaje.objects.get(pk=request.session["oa_pk"])
#     formset = ActividadFormSet(request.POST, instance = oa)
#     title = 'Guardar Actividades OA'
#     context = {
#             "title": title,
#         }
#     for form in formset:
#         print form.as_p
#     if formset.is_valid():
#         for f_form in formset:
#             if f_form.is_valid():
#                 titulo = f_form.cleaned_data.get("titulo")
#                 descripcion = f_form.cleaned_data.get("descripcion")
#                 enunGeneral = f_form.cleaned_data.get("enunGeneral")
#                 objetoAprendizaje = f_form.cleaned_data.get("objetoAprendizaje")
#                 contenido = Contenido(titulo = titulo, descripcion = descripcion, enunGeneral = enunGeneral, objetoAprendizaje = objetoAprendizaje)
#                 contenido.save()
#         return index(request)
#     else:
#         return ayuda(request)
