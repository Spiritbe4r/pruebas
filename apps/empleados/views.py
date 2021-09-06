from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView, FormView

from apps.empleados.forms import EmpleadoForm
from apps.empleados.models import Empleado


class Inicio(TemplateView):
    template_name = 'home.html'


class Empleados:
    pass


class EmpleadoListView(ListView):
    template_name = 'empleados/empleados_list.html'
    model = Empleados
    paginate_by = 3

class EmpleadoByAreaListView(ListView):
    template_name = 'empleados/empleados_byarea.html'
    model = Empleado
    context_object_name = 'empleados_dep'
    #queryset =

    def get_queryset(self):
        area=self.kwargs['depart_name']
        lista=Empleado.objects.filter(departament__name=area)
        return lista

class EmpleadoByKwordListView(ListView):
    template_name = 'empleados/by_kword.html'
    model = Empleado
    context_object_name = 'empleados'
    #queryset =

    def get_queryset(self):
        print("**********")
        palabra_clave=self.request.GET.get("kword",'')
        print("*--------",palabra_clave)
        lista = Empleado.objects.filter(firstname=palabra_clave)
        return lista

class EmpleadoHabilidadesListView(ListView):
    template_name = 'empleados/habilidades.html'
    model = Empleado
    context_object_name = 'habilidades'
    #queryset =

    def get_queryset(self):
        print("**********")
        #palabra_clave=self.request.GET.get("kword",'')
        #print("*--------",palabra_clave)
        empleado = Empleado.objects.get(id=2)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']='empleado del mes'
        return context
class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    #fields = ('firstname','last_name','job','habilidades','departament')
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:success')

    def form_valid(self, form):
        print(form)

        empleado=form.save(commit=False)
        empleado.fullname=empleado.firstname+ ' '+empleado.last_name
        empleado.save()
        print(empleado)

        #logica
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    fields = ('firstname', 'last_name', 'job', 'habilidades', 'departament')
    model = Empleado
    success_url = reverse_lazy('empleados:success')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request,*args,**kwargs)

    def form_valid(self, form):

        #logica
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    template_name = "empleados/delete.html"
    #fields = ('firstname', 'last_name', 'job', 'habilidades', 'departament')
    model = Empleado
    success_url = reverse_lazy('empleados:success')

    def delete(self,request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

