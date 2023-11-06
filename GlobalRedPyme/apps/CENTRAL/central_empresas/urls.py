from django.urls import path, include
from .views import (
    empresas_create,
    empresas_list,
    empresas_listOne,
    empresas_listOne_url,
    empresas_listOne_url_clientes,
    empresas_update,
    empresas_delete,
)

# La variable app_name se utiliza para hacer referencia en el proyecto
app_name = 'central_empresas'

# La variable urlpatters se usa para configurar las rutas en el proyecto en el archivo settings
urlpatterns = [
    path('create/', empresas_create, name="empresas_create"),
    path('list/', empresas_list, name="empresas_list"),
    path('listOne/<str:pk>', empresas_listOne, name="empresas_listOne"),
    path('url/<str:pk>', empresas_listOne_url, name="empresas_listOne"),
    path('urlClientes/<str:pk>', empresas_listOne_url_clientes, name="empresas_listOne_url_clientes"),
    path('update/<str:pk>', empresas_update, name="empresas_update"),
    path('delete/<str:pk>', empresas_delete, name="empresas_delete"),
]
