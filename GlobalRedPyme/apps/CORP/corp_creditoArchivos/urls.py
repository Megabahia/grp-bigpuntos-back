from django.urls import path, include
from .views import (
    creditoArchivos_create,
    creditoArchivos_list,
    creditoArchivos_delete,
    uploadEXCEL_creditosPreaprobados,
    uploadEXCEL_creditosPreaprobados_empleados,
    uploadEXCEL_creditosPreaprobados_negocios,
    viewEXCEL_creditosPreaprobados_negocios,
)

app_name = 'corp_creditoArchivos'

urlpatterns = [
    path('create/', creditoArchivos_create, name="creditoArchivos_create"),
    path('list/', creditoArchivos_list, name="creditoArchivos_list"),
    path('delete/<int:pk>', creditoArchivos_delete, name="creditoArchivos_delete"),
    path('upload/creditos/preaprobados/<int:pk>', uploadEXCEL_creditosPreaprobados,
         name="uploadEXCEL_creditosPreaprobados"),
    path('upload/creditos/preaprobados/empleados/<int:pk>', uploadEXCEL_creditosPreaprobados_empleados,
         name="uploadEXCEL_creditosPreaprobados_empleados"),
    path('upload/creditos/preaprobados/negocios/<int:pk>', uploadEXCEL_creditosPreaprobados_negocios,
         name="uploadEXCEL_creditosPreaprobados_negocios"),
    path('view/creditos/preaprobados/negocios/<int:pk>', viewEXCEL_creditosPreaprobados_negocios,
         name="viewEXCEL_creditosPreaprobados_negocios"),
]
