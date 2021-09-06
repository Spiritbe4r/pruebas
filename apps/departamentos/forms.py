from django import forms
from django.forms import TextInput


class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    # short_name = forms.CharField(max_length=20)
    shortname = forms.CharField(max_length=50)

    widgets = {
        'nombre': forms.TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Ingrese nombres'
        }),
        'apellidos': forms.TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Ingrese apellidos'
        }),
        'department': TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Ingrese nombres departamento'
        }),
        'shortname': TextInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Ingrese nombres corto de departamento'
        }),
    }