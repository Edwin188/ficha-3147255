from django import forms
from .models import actividad

class CrearFom(forms.ModelForm):
    class Meta:
        model = actividad
        fields = ['titulo', 'descripcion', 'importante']
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a titulo'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a descripcion'}),
            'importante' : forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }