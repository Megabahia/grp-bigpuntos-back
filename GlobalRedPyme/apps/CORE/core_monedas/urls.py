from django.urls import path,include
from apps.CORE.core_monedas.views import(
	monedas_create,
	monedas_list,
	monedas_listOne,
	monedas_update,
	monedas_delete
)
app_name = 'core_monedas'

urlpatterns = [
	path('create/', monedas_create, name="monedas_create"),
	path('list/', monedas_list, name="monedas_list"),
	path('listOne/<str:pk>', monedas_listOne, name="monedas_listOne"),
	path('update/<str:pk>', monedas_update, name="monedas_update"),
	path('delete/<str:pk>', monedas_delete, name="monedas_delete"),
]

