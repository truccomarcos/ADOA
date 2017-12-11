from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet, formset_factory
from django.forms.formsets import BaseFormSet
from models import *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.bootstrap import *
from djangoformsetjs.utils import formset_media_js
import pdb

class ObjetoAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ObjetoAprendizaje
        fields = ['titulo','patron','descripcion']
    titulo = forms.CharField(max_length = 30)
    descripcion = forms.CharField(widget=CKEditorWidget())
    patron = forms.ModelChoiceField(queryset=Patron.objects.all())
    def __init__(self, *args, **kwargs):
        super(ObjetoAprendizajeForm, self).__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('patron'),
                HTML("<a href= '{% url 'adoa:patrones' %}''>Que patron elegir? </a>"),
                Field('titulo'),
                Field('descripcion'),
                # HTML('<input type="submit" class="btn btn-primary" value="Continuar &rarr;">'),
        css_class='row-fluid'),
        )

#--------------------------------------------------------------------------
class PatronForm(ModelForm):
    class Meta:
        model = Patron
        fields = ['titulo', 'descripcion', 'problemas', 'solucion']


# #--------------------------------------------------------------------------
class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['orden','titulo','descripcion','contenido']
    orden = forms.IntegerField()
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=300)
    contenido = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('orden',type='hidden'),
                Field('titulo'),
                Field('descripcion'),
                Field('contenido'),
                css_class='row-fluid'),
            )
        super(ContenidoForm, self).__init__(*args, **kwargs)


ObjetoAprendizajeInlineFormSet = inlineformset_factory(ObjetoAprendizaje,
    Contenido,
    form=ContenidoForm,
    extra=0,
    can_delete=False,
    can_order=False
)

ContenidoFormSet = formset_factory(ContenidoForm)
#--------------------------------------------------------------------------
# class ActividadForm(forms.ModelForm):
#     class Meta:
#         model = Actividad
#         fields = ['enunciado','tipo']
#     enunciado = forms.CharField(max_length=100)
#     def __init__(self, *args, **kwargs):
#         self.helper= FormHelper()
#         self.helper.layout = Layout(
#             Div(
#                 Div('enunciado'),
#                 Div('tipo'),
#             css_class='row-fluid'),
#         )
#         super(ActividadForm, self).__init__(*args, **kwargs)

class ElementoVoFForm(forms.ModelForm):
    class Meta:
        model = ElementoVoF
        fields = ['enunciado','verdad']

class ElementoAsociacionForm(forms.ModelForm):
    class Meta:
        model = ElementoAsociacion
        fields = ['enunciado','imagen']

class ElementoIdentificacionForm(forms.ModelForm):
    class Meta:
        model = ElementoIdentificacion
        fields = ['enunciado','correcto']

class ElementoOpcionMultipleForm(forms.ModelForm):
    class Meta:
        model = ElementoOpcionMultiple
        fields = ['enunciado','correcta','incorrecta1','incorrecta2','incorrecta3']

class ElementoOrdenamientoForm(forms.ModelForm):
    class Meta:
        model = ElementoOrdenamiento
        fields = ['enunciado','orden']
#--------------------------------------------------------------------------
#
# ObjetoAprendizajeInlineFormset = inlineformset_factory(ObjetoAprendizaje,
#                                          Contenido,
#                                          form=ContenidoForm,
#                                          fields=('titulo','descripcion','contenido')
#                                          )

# ActvidadesFormSet = inlineformset_factory(ObjetoAprendizaje, Actividad,
#     form=ActividadForm, extra=2)

#-------------------------------------------------------------------------
class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

#--------------------------------------------------------------------------
# class ElementoVerdaderoFalsoForm(forms.ModelForm):
#     class Meta:
#         model = ElementoVoF
#         fields = ['enunciado', 'verdad']
#     enunciado = forms.CharField(max_length = 30)
#     verdad = forms.BooleanField()
#     def __init__(self, *args, **kwargs):
#         self.helper= FormHelper()
#         self.helper.layout = Layout(
#             Div(
#                 Div('enunciado'),
#                 Div('verdad '),
#             css_class='row-fluid'),
#         )
#         super(ActividadForm, self).__init__(*args, **kwargs)

#--------------------------------------------------------------------------
# class ContenidoFormSet(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         contenidos = []
#
# class ActividadesFormSet(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         actividades = []

#--------------------------------------------------------------------------
# class VerdaderoFalsoFormset(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         VoFs = []

# class BaseNestedFormset(BaseInlineFormSet):
#
#     def add_fields(self, form, index):
#         # allow the super class to create the fields as usual
#         super(BaseNestedFormset, self).add_fields(form, index)
#         form.nested = self.nested_formset_class(
#             instance=form.instance,
#             data=form.data if self.is_bound else None,
#             prefix='%s-%s' % (
#                 form.prefix,
#                 self.nested_formset_class.get_default_prefix(),
#             ),
#         )
#
#     def is_valid(self):
#         result = super(BaseNestedFormset, self).is_valid()
#         if self.is_bound:
#             # look at any nested formsets, as well
#             for form in self.forms:
#                 result = result and form.nested.is_valid()
#         return result
#
#     def save(self, commit=True):
#         result = super(BaseNestedFormset, self).save(commit=commit)
#         for form in self:
#             form.nested.save(commit=commit)
#         return result
#
# def nested_formset_factory(parent_model, child_model, grandchild_model):
#     parent_child = inlineformset_factory(
#         parent_model,
#         child_model,
#         formset=BaseNestedFormset,
#     )
#     parent_child.nested_formset_class = inlineformset_factory(
#         child_model,
#         grandchild_model,
#     )
#     return parent_child


    # def add_fields(self, form, index):
    #         # allow the super class to create the fields as usual
    #         super(ActividadesFormSet, self).add_fields(form, index)
    #         form.nested = self.nested_formset_class(
    #             instance=form.instance,
    #             data=form.data if self.is_bound else None,
    #             prefix='%s-%s' % (
    #                 form.prefix,
    #                 self.nested_formset_class.get_default_prefix(),
    #         ),
    #     )
