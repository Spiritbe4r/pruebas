from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from apps.departamentos.forms import NewDepartmentForm
from apps.departamentos.models import Departamento

from apps.empleados.models import Empleado


class NewDeparment(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartmentForm
    success_url = '/'

    def form_valid(self, form):

        depa=Departamento(
            name=form.cleaned_data['departament'],
            short_name=form.cleaned_data['shortname'],
        )
        depa.save()
        nombre=form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            firstname=nombre,
            last_name=apellido,
            job="ECONOMISTA",
            department=depa
        )
        return super(NewDeparment,self).form_valid(form)