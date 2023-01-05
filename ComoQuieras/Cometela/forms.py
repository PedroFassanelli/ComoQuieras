from django import forms
from django.forms import formset_factory

from Cometela.models import Vianda

class FormCargaVianda(forms.ModelForm):

    class Meta:
        model = Vianda
        
        fields = ('dia', 'fecha','descripcion','tipo' )

        def __init__(self, *args, **kwargs):
            super(FormCargaVianda, self).__init__(*args, **kwargs)

            self.fields['dia'].widget.attrs['class'] = 'form-control'
            self.fields['dia'].widget.attrs['placeholder'] = "DIA"

            self.fields['fecha'].widget.attrs['class'] = 'text'
            self.fields['fecha'].widget.attrs['placeholder'] = "Fecha"

            self.fields['descripcion'].widget.attrs['class'] = 'form-control'
            self.fields['descripcion'].widget.attrs['placeholder'] = "Menú"

            self.fields['tipo'].widget.attrs['class'] = 'form-control'
            self.fields['tipo'].widget.attrs['placeholder'] = "Tipo"

#TODO ver esto
class FormCargaSemana(forms.Form):

    precio_media = forms.IntegerField()
    precio_entera = forms.IntegerField()

    #LUNES
    fecha1 = forms.DateField()
    menu1 = forms.CharField(max_length=250)
    menu2 = forms.CharField(max_length=250)
    menu3 = forms.CharField(max_length=250)

    #MARTES
    fecha2 = forms.DateField()
    menu4 = forms.CharField(max_length=250)
    menu5 = forms.CharField(max_length=250)
    menu6 = forms.CharField(max_length=250)
    
    #MIERCOLES
    fecha3 = forms.DateField()
    menu7 = forms.CharField(max_length=250)
    menu8 = forms.CharField(max_length=250)
    menu9 = forms.CharField(max_length=250)

    #JUEVES
    fecha4 = forms.DateField()
    menu10 = forms.CharField(max_length=250)
    menu11 = forms.CharField(max_length=250)
    menu12 = forms.CharField(max_length=250)

    #VIERNES
    fecha5 = forms.DateField()
    menu13 = forms.CharField(max_length=250)
    menu14 = forms.CharField(max_length=250)
    menu15 = forms.CharField(max_length=250)
    



