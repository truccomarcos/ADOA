from django.template import loader, Context
from django.http import HttpResponse,HttpResponseRedirect
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
from django.views import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from .models import ObjetoAprendizaje


from django.core import serializers
from django.http import JsonResponse
from extra_views import FormSetView, ModelFormSetView, InlineFormSetView, InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, CalendarMonthView, NamedFormsetsMixin, SortableListMixin, SearchableListMixin
from extra_views.generic import GenericInlineFormSet, GenericInlineFormSetView

class ObjetoAprendizajeList(ListView):
    model = ObjetoAprendizaje

class ObjetoAprendizajeDetail(DetailView):
    model = ObjetoAprendizaje

class GetContenidoPatron(View):
    def get(self,request,pk):
        patron = Patron.objects.get(pk=pk)
        contenidos = patron.contenidopatron_set.values('orden','descripcion')
        return JsonResponse({'contenidos': list(contenidos)})

class ContenidoCreate(ModelFormSetView):
    model = Contenido
    form_class = ContenidoForm
    template_name = 'adoa/contenido_form.html'

class ContenidoInline(InlineFormSet):
    model = Contenido
    form_class = ContenidoForm

class ContenidoView(ModelFormSetView):
    model = Contenido
    fields = ['orden','titulo','descripcion','contenido']
    form_class = ContenidoForm
    template_name = 'adoa/contenido_form.html'
    def get(self,request,pk):
        patron_id = self.kwargs['pk']
        contenidos = Patron.objects.get(pk=patron_id).contenidopatron_set.values()
        self.extra = len(contenidos)
        return super(ContenidoView, self).get(self,request)
    def get_initial(self):
        patron_id = self.kwargs['pk']
        contenidos = Patron.objects.get(pk=patron_id).contenidopatron_set.values()
        return contenidos

class ObjetoAprendizajeCreate(CreateWithInlinesView):
    model = ObjetoAprendizaje
    form_class = ObjetoAprendizajeForm
    inlines = [ContenidoInline]
    template_name = 'adoa/objeto_and_contenidos.html'
    # def form_valid(self,request):
    #     form = self.form_class(self.request.POST)
    #     objetoAprendizaje = form.save(commit=False)
    #     objetoAprendizaje.user = self.request.user
    #     objetoAprendizaje.save()
    #     return HttpResponseRedirect(reverse_lazy('adoa:list', kwargs={'pk':objetoAprendizaje.id}))





# class CreateOAView(CreateView):
#     model = ObjetoAprendizaje
#     form_class = ObjetoAprendizajeForm # the parent object's form
#
#     # On successful form submission
#     def get_success_url(self):
#         return reverse('adoa:list')
#
#     # Validate forms
#     def form_valid(self, form):
#         ctx = self.get_context_data()
#         inlines = ctx['inlines']
#         if inlines.is_valid() and form.is_valid():
#             self.object = form.save() # saves Father and Children
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
#
#     # We populate the context with the forms. Here I'm sending
#     # the inline forms in `inlines`
#     def get_context_data(self, **kwargs):
#         ctx = super(CreateOAView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             ctx['form'] = ObjetoAprendizajeForm(self.request.POST)
#             ctx['inlines'] = ObjetoAprendizajeInlineFormSet(self.request.POST)
#         else:
#             ctx['form'] = ObjetoAprendizajeForm()
#             ctx['inlines'] = ObjetoAprendizajeInlineFormSet()
        # return ctx


# class ObjetoAprendizajeCreation(CreateView):
#     model = ObjetoAprendizaje
#     form_class = ObjetoAprendizajeForm
#     def form_valid(self, form):
#         objetoAprendizaje = form.save(commit=False)
#         objetoAprendizaje.user = self.request.user
#         objetoAprendizaje.save()
#         return HttpResponseRedirect(reverse_lazy('adoa:contenidos', kwargs={'pk':objetoAprendizaje.id}))
#

# class ContenidosCreation(View):
#     model = Contenido
#     formset_class = formset_factory(ContenidoForm)
#     template_name = 'adoa/contenido_form.html'
#     def get(self, request,pk):
#             oa = request.session['oa']
#             contenidos = request.session['contenidos']
#             contenidos_data = [{'orden': int(c['orden']), 'titulo': str(c['titulo']), 'descripcion': str(c['descripcion']), 'contenido': str(c['contenido'])}
#                             for c in request.session['contenidos']]
#             formset = self.formset_class(initial = contenidos_data)
#             return render(request, self.template_name, { 'oa':oa, 'contenido_formset': formset })
#
#     def get_context_data(self, **kwargs):
#         context = super(ContenidosCreation, self).get_context_data(**kwargs)
#         context['pk'] = self.kwargs['pk']
#         context['form-template'] = ContenidoForm
#         return context
#     def get_initial(self):
#         pk = self.kwargs['pk']
#         objetoAprendizaje = ObjetoAprendizaje.objects.get(pk=pk)
#         initial = objetoAprendizaje.patron.contenidopatron_set.values()
#         return initial
#     def form_valid(self, form):
#         pdb.set_trace()
#         pk = self.kwargs['pk']
#         oa = ObjetoAprendizaje.objects.get(pk=pk)
#         contenidos = form.save(commit=False)
#         for contenido in contenidos:
#             contenido.objetoAprendizaje = oa
#         contenidos.save()
#         return reverse_lazy('adoa:list')






# class CreateFatherView(CreateView):
#     template_name = 'father_create.html'
#     model = Father
#     form_class = FatherForm # the parent object's form
#
#     # On successful form submission
#     def get_success_url(self):
#         return reverse('father-created')
#
#     # Validate forms
#     def form_valid(self, form):
#         ctx = self.get_context_data()
#         inlines = ctx['inlines']
#         if inlines.is_valid() and form.is_valid():
#             self.object = form.save() # saves Father and Children
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
#
#     # We populate the context with the forms. Here I'm sending
#     # the inline forms in `inlines`
#     def get_context_data(self, **kwargs):
#         ctx = super(CreateFatherView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             ctx['form'] = FatherForm(self.request.POST)
#             ctx['inlines'] = FatherInlineFormSet(self.request.POST)
#         else:
#             ctx['form'] = Father()
#             ctx['inlines'] = FatherInlineFormSet()
#         return ctx




class ObjetoAprendizajeUpdate(UpdateView):
    model = ObjetoAprendizaje
    success_url = reverse_lazy('adoa:list')
    fields = ['titulo', 'patron', 'descripcion']

class ObjetoAprendizajeDelete(DeleteView):
    model = ObjetoAprendizaje
    success_url = reverse_lazy('adoa:list')


class Index(View):
    def get(self,request):
        context = {
            'title': 'index',
            'form': UserLoginForm(request.POST or None)
        }
        return render(request, 'index.html', context)

class QueEsOA(View):
    def get(self,request):
        context = {
            'title':'Que es un Objeto de Aprendizaje?',
        }
        return render(request, 'queEsOA.html', context)

class QueEsPatron(View):
    def get(self,request):
        context = {
            'title':'Que es un Patron de Aprendizaje?',
        }
        return render(request, 'queEsPatron.html', context)

class Ayuda(View):
    def get(self,request):
        context = {
            'title':'Ayuda',
        }
        return render(request, 'ayuda.html', context)

class PatronesView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Patrones',
            'patrones': Patron.objects.all()
        }
        return render(request, 'patrones.html', context)

# class OAFormView(View):
#     form_class = ObjetoAprendizajeForm
#     template_name = 'oa_edit.html'
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             oa = form.save(*)
#             contenidos = oa.patron.get_contenidos()
#             contenidos_serial = []
#             for contenido in contenidos:
#                 contenidos_serial.append(model_to_dict(contenido))
#             request.session['oa'] = model_to_dict(oa)
#             request.session['contenidos'] = contenidos_serial
#             return redirect('oa_contenidos')
#         return render(request, self.template_name, {'form': form})
#
# class OAContenidosFormView(View):
#     formset_class = formset_factory(ContenidoForm, formset=ContenidosFormSet)
#     template_name = 'oa_contenidos.html'
#     def get(self, request, *args, **kwargs):
#         oa = request.session['oa']
#         contenidos = request.session['contenidos']
#         contenidos_data = [{'orden': int(c['orden']), 'titulo': str(c['titulo']), 'descripcion': str(c['descripcion']), 'contenido': str(c['contenido'])}
#                         for c in request.session['contenidos']]
#         formset = self.formset_class(initial = contenidos_data)
#         return render(request, self.template_name, { 'oa':oa, 'contenido_formset': formset })
#     def post(self, request, *args, **kwargs):
#         contenido_formset = self.formset_class(request.POST)
#         if contenido_formset.is_valid():
#             contenidos = []
#             for contenido_form in contenido_formset:
#                 contenidos.append(model_to_dict(contenido_form.save(commit=False)))
#             request.session['contenidos'] = contenidos
#             return redirect('oa_actividades')
#         return render(request, self.template_name, { 'oa':oa, 'contenido_formset': contenido_formset })
#
# class OAActividadesFormView(View):
#     formset_class = formset_factory(ActividadForm, formset=ActividadesFormSet)
#     template_name = 'oa_actividades.html'
#     def get(self, request, *args, **kwargs):
#         oa = request.session['oa']
#         formset = self.formset_class()
#         return render(request, self.template_name, { 'oa':oa, 'actividades_formset': formset })
#     def post(self, request, *args, **kwargs):
#         actividades_formset = self.formset_class(request.POST)
#         if actividades_formset.is_valid():
#             actividades = []
#             for actividad_form in actividades_formset:
#                 actividades.append(model_to_dict(actividad_form.save(commit=False)))
#             request.session['actividades'] = actividades
#             return redirect('oa_final')
#         return render(request, self.template_name, { 'oa':oa, 'actividades_formset': actividades_formset })
#
# class OAFinalView(View):
#     def get(self, request, *args, **kwargs):
#         oa = request.session['oa']
#         contenidos = request.session['contenidos']
#         actividades = request.session['actividades']
#         return render(request, 'save_oa_details.html', {'oa': oa,'contenidos': contenidos, 'actividades':actividades})
#     def post(self, request, *args, **kwargs):
#         oa = bunchify(request.session['oa'])
#         contenidos = bunchify(request.session['contenidos'])
#         actividades = bunchify(request.session['actividades'])
#         newOa = ObjetoAprendizaje(titulo= oa.titulo, descripcion= oa.descripcion, patron= Patron.objects.get(id=oa.patron), user= User.objects.get(username = request.user))
#         newOa.save()
#         for contenido in contenidos:
#             newOa.contenido_set.create(orden= contenido.orden, titulo= contenido.titulo, descripcion=contenido.descripcion, contenido= contenido.contenido)
#         for actividad in actividades:
#             newOa.actividad_set.create(enunciado= actividad.enunciado, tipo=actividad.tipo)
#         return render(request, 'oa_final.html', {'oa': model_to_dict(newOa), 'contenidos': contenidos, 'actividades': actividades})
