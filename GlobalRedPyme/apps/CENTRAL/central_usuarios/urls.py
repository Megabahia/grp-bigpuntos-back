from django.urls import path,include
from apps.CENTRAL.central_usuarios.views import(
	usuario_list,
	usuario_listExport,
	usuario_create,
	usuario_findOne,
	usuario_update,
	usuario_delete,
	usuarioImagen_update,
	vendedor_list,
	usuarios_list_rol,
	usuario_core_create
)
app_name = 'usuarios'

urlpatterns = [
	path('list/', usuario_list, name="usuario_list"),
	path('list/export/', usuario_listExport, name="usuario_export"),
	path('create/', usuario_create, name="usuario_create"),
	path('corp/create/', usuario_core_create, name="usuario_core_create"),
	path('listOne/<str:pk>', usuario_findOne, name="usuario_findOne"),
	path('update/<str:pk>', usuario_update, name="usuario_update"),
	path('delete/<str:pk>', usuario_delete, name="usuario_delete"),
	path('update/imagen/<str:pk>', usuarioImagen_update, name="usuarioImagen_update"),
	path('list/vendedor/', vendedor_list, name="vendedor_list"),
	path('list/rol/', usuarios_list_rol, name="usuarios_list_rol"),
]

