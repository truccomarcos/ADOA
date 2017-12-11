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
#--------------------------------------------------------------------------

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

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

#--------------------------------------------------------------------------
