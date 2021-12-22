from django.urls import path,include
from apps.CORP.corp_creditoPersonas.views import(
	creditoPersonas_create,
	creditoPersonas_listOne,
	creditoPersonas_update,
	creditoPersonas_delete,
	creditoPersonas_list,
)
app_name = 'corp_creditoPersonas'

urlpatterns = [
	path('create/', creditoPersonas_create, name="creditoPersonas_create"),
	path('list/', creditoPersonas_list, name="creditoPersonas_list"),
	path('listOne/<str:pk>', creditoPersonas_listOne, name="creditoPersonas_listOne"),
	path('update/<str:pk>', creditoPersonas_update, name="creditoPersonas_update"),
	path('delete/<str:pk>', creditoPersonas_delete, name="creditoPersonas_delete"),
]

