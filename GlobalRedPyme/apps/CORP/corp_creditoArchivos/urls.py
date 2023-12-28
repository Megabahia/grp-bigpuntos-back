from django.urls import path, include
from .views import (
    creditoArchivos_create,
    creditoArchivos_list,
    creditoArchivos_delete,
    uploadEXCEL_creditosPreaprobados,
    uploadEXCEL_creditosPreaprobados_empleados,
    uploadEXCEL_creditosPreaprobados_negocios,
    viewEXCEL_creditosPreaprobados_negocios,
    uploadEXCEL_creditosPreaprobados_automotriz_empleados,
    comisiones_list, comisionesArchivos_create, comisiones_delete, uploadEXCEL_comisiones, viewEXCEL_comisiones,
)

# Esta variable se utiliza para colocar el nombre aplicacion de corp_creditoArchivos
app_name = 'corp_creditoArchivos'

# La variable urlpatterns se utiliza para exportar las diferentes rutas a las que pueden acceder el front
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
    path('upload/creditos/preaprobados/automotriz/empleados/<int:pk>',
         uploadEXCEL_creditosPreaprobados_automotriz_empleados,
         name="uploadEXCEL_creditosPreaprobados_automotriz_empleados"),
    path('create/comisiones/', comisionesArchivos_create, name="comisionesArchivos_create"),
    path('list/comisiones/', comisiones_list, name="comisiones_list"),
    path('delete/comisiones/<str:pk>', comisiones_delete, name="comisiones_delete"),
    path('upload/comisiones/<str:pk>', uploadEXCEL_comisiones, name="uploadEXCEL_comisiones"),
    path('view/comisiones/<str:pk>', viewEXCEL_comisiones, name="viewEXCEL_comisiones"),
]
