from django.contrib import admin

# Register your models here.
from apps.empleados.models import Empleado, Habilidades

admin.site.register(Empleado)
admin.site.register(Habilidades)