from django.db import models

# Create your models here.
from apps.departamentos.models import Departamento
class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    def __str__(self):
        return self.habilidad

class Empleado(models.Model):
    class JOBS(models.TextChoices):
        CONTADOR = "CONTADOR", "Contador"
        ADMINISTRADOR = "ADMINISTRADOR", "Administrador"
        ECONOMISTA = "ECONOMISTA", "Economista"
        OTROS = "OTROS", "Otros"

    firstname = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    fullname = models.CharField('nombre completo', max_length=50,blank=True, null=True)
    job = models.CharField('Trabajo', choices=JOBS.choices, max_length=50)
    departament=models.ForeignKey(Departamento,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado/',blank=True,null=True)
    habilidades=models.ManyToManyField(Habilidades,related_name="empleado_habilidad")

    


    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Empleados"
        ordering=['-firstname']
    def __str__(self):
        return f'{self.firstname} {self.last_name}'