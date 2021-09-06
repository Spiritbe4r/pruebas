from django import forms

from apps.empleados.models import Empleado


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model=Empleado
        fields="__all__"

    widgets={
        'firstname':forms.TextInput(
            attrs={
                'placeholder':'Ingrese el Primer Nombre',
                'class':'form-control'
            }
        )
    }

    def clean_firstname(self):
        fname=self.cleaned_data['firstname']
        if not fname.isalpha():
            raise forms.ValidationError("first name is only alfa numerics")

        return fname


