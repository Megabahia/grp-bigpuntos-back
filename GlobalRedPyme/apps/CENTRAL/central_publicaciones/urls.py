from django.urls import path
from .views import (
    publicaciones_create,
    publicaciones_list,
    publicaciones_listOne,
    publicaciones_update,
    publicaciones_delete,
    publicaciones_imagenUpdate,
    publicaciones_compartir,
    publicaciones_usuario,
    publicaciones_list_full,
    publicaciones_reporte,
)

app_name = 'central_publicaciones'

urlpatterns = [
    path('create/', publicaciones_create, name="publicaciones_create"),
    path('list/', publicaciones_list, name="publicaciones_list"),
    path('listFull/', publicaciones_list_full, name="publicaciones_list_full"),
    path('listOne/<str:pk>', publicaciones_listOne, name="publicaciones_listOne"),
    path('update/<str:pk>', publicaciones_update, name="publicaciones_update"),
    path('delete/<str:pk>', publicaciones_delete, name="publicaciones_delete"),
    path('update/imagen/<str:pk>', publicaciones_imagenUpdate, name="publicaciones_imagenUpdate"),
    path('compartir/', publicaciones_compartir, name="publicaciones_compartir"),
    path('usuario/', publicaciones_usuario, name="publicaciones_usuario"),
    path('reporte/', publicaciones_reporte, name="publicaciones_reporte"),
]
