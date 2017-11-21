from django import forms
from django.forms import ModelForm, inlineformset_factory
from models import *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.bootstrap import *


class ObjetoAprendizajeForm(forms.Form):
    # class Meta:
    #     model = ObjetoAprendizaje
    #     fields = ["patron", "titulo" , "descripcion"]
    titulo = forms.CharField(max_length = 30)
    descripcion = forms.CharField(widget=CKEditorWidget())
    patron = forms.ModelChoiceField(queryset=Patron.objects.all())
    def __init__(self, *args, **kwargs):

        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('Objeto de Aprendizaje'),
                Div('patron', HTML("<a href= '{% url 'patrones' %}''>Que patron elegir? </a>"),),
                Div('titulo', ),
                Div('descripcion', ),
                HTML("<div class='well'><center><button type='submit' class='btn btn-success' >Guardar y contiunar</button></center></div>"),
                # Submit('contunuar', 'Guardar y Continuar'),
        css_class='row-fluid'),

        )
        super(ObjetoAprendizajeForm, self).__init__(*args, **kwargs)


class PatronForm(ModelForm):
    class Meta:
        model = Patron
        fields = ['titulo', 'descripcion', 'problemas', 'solucion']


class ContenidoForm(forms.Form):
    # class Meta:
    #     model = Contenido
    #     fields = ['orden','titulo','descripcion','contenido','objetoAprendizaje']
    orden = forms.IntegerField()
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    contenido = forms.CharField(widget=CKEditorWidget())
    # objetoAprendizaje = forms.ModelChoiceField(queryset=ObjetoAprendizaje.objects.all(), initial = ObjetoAprendizaje.objects.get(pk=1))
    def __init__(self, *args, **kwargs):
        self.helper= FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(''),
                HTML("<h1>{{form.orden.value}})  {{form.titulo.value}}</h1>"),
                HTML("<h3>{{form.descripcion.value}}</h2>  "),
                HTML("<textarea name='contenido_{{form.orden.value}}' class='ckeditor'></textarea>"),



            css_class='row-fluid'),
        )

        super(ContenidoForm, self).__init__(*args, **kwargs)




class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class VerdaderoFalsoForm(forms.Form):
    enunGeneral =  forms.CharField(max_length = 30)
    descripcion = forms.CharField(widget=CKEditorWidget())
    # objetoAprendizaje = forms.ModelChoiceField(queryset=ObjetoAprendizaje.objects.all(), initial = ObjetoAprendizaje.objects.get(pk=1))

class ElementoVerdaderoFalsoForm(forms.Form):
    enunciado = forms.CharField(max_length = 30)
    verdad = forms.BooleanField()
    VoF = forms.ModelChoiceField(queryset=VerdaderoFalso.objects.all())
