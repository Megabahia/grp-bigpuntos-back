from django.urls import path
from .views import (
    productos_create,
    productos_list,
    productos_listOne,
    productos_update,
    productos_delete,
    productos_imagenUpdate,
    productos_list_vigencia,
    productos_list_free,
    productos_list_free_landing,
    productos_create_landing,
    productos_update_landing,
    productos_listOne_landing,
    productos_delete_landing,
)

app_name = 'central_productos'

urlpatterns = [
    path('create/', productos_create, name="productos_create"),
    path('create-landing/', productos_create_landing, name="productos_create_landing"),
    path('list/', productos_list, name="productos_list"),
    path('list-free/', productos_list_free, name="productos_list_free"),
    path('list-free-landing/', productos_list_free_landing, name="productos_list_free_landing"),
    path('listOne/<str:pk>', productos_listOne, name="productos_listOne"),
    path('listOne-landing/<str:pk>', productos_listOne_landing, name="productos_listOne_landing"),
    path('update/<str:pk>', productos_update, name="productos_update"),
    path('update-landing/<str:pk>', productos_update_landing, name="productos_update_landing"),
    path('delete/<str:pk>', productos_delete, name="productos_delete"),
    path('delete-landing/<str:pk>', productos_delete_landing, name="productos_delete_landing"),
    path('update/imagen/<str:pk>', productos_imagenUpdate, name="productos_imagenUpdate"),
    path('list/vigencia', productos_list_vigencia, name="productos_list_vigencia"),
]
