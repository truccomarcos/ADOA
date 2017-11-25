from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.forms.formsets import BaseFormSet
from models import *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.bootstrap import *
import pdb


class ObjetoAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ObjetoAprendizaje
        fields = ['titulo','descripcion','patron']
    titulo = forms.CharField(max_length = 30)
    descripcion = forms.CharField(widget=CKEditorWidget())
    patron = forms.ModelChoiceField(queryset=Patron.objects.all())
    def __init__(self, *args, **kwargs):
        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('Objeto de Aprendizaje'),
                Div('patron', HTML("<a href= '{% url 'patrones' %}''>Que patron elegir? </a>"),),
                Div('titulo'),
                Div('descripcion'),
                HTML("<div class='well'><center><button type='submit' class='btn btn-success' >Contiunar</button></center></div>"),
                # Submit('contunuar', 'Guardar y Continuar'),
        css_class='row-fluid'),
        )
        super(ObjetoAprendizajeForm, self).__init__(*args, **kwargs)


class PatronForm(ModelForm):
    class Meta:
        model = Patron
        fields = ['titulo', 'descripcion', 'problemas', 'solucion']


class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['orden','titulo','descripcion','contenido']
    orden = forms.IntegerField()
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=CKEditorWidget())
    contenido = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('Contenido'),
                Div('orden'),
                Div('titulo'),
                Div('descripcion'),
                Div('contenido'),
            css_class='row-fluid'),
        )
        super(ContenidoForm, self).__init__(*args, **kwargs)


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['titulo']
    titulo = forms.CharField(max_length=100)
    def __init__(self, *args, **kwargs):
        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('titulo'),
            css_class='row-fluid'),
        )
        super(ActividadForm, self).__init__(*args, **kwargs)


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class VerdaderoFalsoForm(ActividadForm):
    enunGeneral =  forms.CharField(max_length = 30)
    descripcion = forms.CharField(widget=CKEditorWidget())
    # objetoAprendizaje = forms.ModelChoiceField(queryset=ObjetoAprendizaje.objects.all(), initial = ObjetoAprendizaje.objects.get(pk=1))

class ElementoVerdaderoFalsoForm(forms.Form):
    enunciado = forms.CharField(max_length = 30)
    verdad = forms.BooleanField()
    VoF = forms.ModelChoiceField(queryset=VerdaderoFalso.objects.all())

class ContenidosFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        contenidos = []

class ActividadesFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        actividades = []
