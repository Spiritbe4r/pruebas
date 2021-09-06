
from django.contrib import admin
from django.urls import path

from apps.departamentos.views import NewDeparment
app_name="departamentos"
urlpatterns = [
    path('create/', NewDeparment.as_view(),name="create"),
    #path('prueba/', pruebas),
]
