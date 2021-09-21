from django.urls import path,include
from apps.CENTRAL.central_productos.views import(
	productos_create,
	productos_list,
	productos_listOne,
	productos_update,
	productos_delete
)
app_name = 'central_productos'

urlpatterns = [
	path('create/', productos_create, name="productos_create"),
	path('list/', productos_list, name="productos_list"),
	path('listOne/<str:pk>', productos_listOne, name="productos_listOne"),
	path('update/<str:pk>', productos_update, name="productos_update"),
	path('delete/<str:pk>', productos_delete, name="productos_delete"),
]

