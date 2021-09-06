
from django.contrib import admin
from django.urls import path

from apps.empleados.views import EmpleadoListView, EmpleadoByAreaListView, EmpleadoByKwordListView, \
    EmpleadoHabilidadesListView, EmpleadoDetailView, EmpleadoCreateView, SuccessView, EmpleadoUpdateView, \
    EmpleadoDeleteView

app_name="empleados"
urlpatterns = [
    path('list/', EmpleadoListView.as_view(),name="list_empleados"),
    path('list_byarea/<depart_name>/', EmpleadoByAreaListView.as_view(),name="list_empleados_byarea"),
    path('buscar_empleado/', EmpleadoByKwordListView.as_view(),name="buscar_empleado"),
    path('empleado_habi/', EmpleadoHabilidadesListView.as_view(),name="habilidades_empleado"),
    path('empleado/<int:pk>', EmpleadoDetailView.as_view(),name="empleado_detail"),
    path('create/', EmpleadoCreateView.as_view(),name="empleado_create"),
    path('empleado/', SuccessView.as_view(),name="success"),
    path('update/<int:pk>', EmpleadoUpdateView.as_view(),name="empleado_update"),
    path('delete/<int:pk>', EmpleadoDeleteView.as_view(),name="empleado_delete"),
    #path('prueba/', pruebas),
]
