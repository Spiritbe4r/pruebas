# Generated by Django 3.2.6 on 2021-09-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(related_name='empleado_habilidad', to='empleados.Habilidades'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('CONTADOR', 'Contador'), ('ADMINISTRADOR', 'Administrador'), ('ECONOMISTA', 'Economista'), ('OTROS', 'Otros')], max_length=50, verbose_name='Trabajo'),
        ),
    ]