from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shortname = models.CharField('Nombre corto', max_length=50)
    anulate = models.BooleanField('Anulado' ,default=False)
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        
    def __str__(self):
        return self.name + '-' + self.shortname