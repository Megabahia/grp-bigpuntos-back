from django.urls import path,include
from apps.CORP.corp_creditoArchivos.views import(
	creditoArchivos_create,
	creditoArchivos_list,
	creditoArchivos_delete,
	creditoArchivos_subir,
)
app_name = 'corp_creditoArchivos'

urlpatterns = [
	path('create/', creditoArchivos_create, name="creditoArchivos_create"),
	path('list/', creditoArchivos_list, name="creditoArchivos_list"),
	path('delete/<int:pk>', creditoArchivos_delete, name="creditoArchivos_delete"),
	path('subir/<int:pk>', creditoArchivos_subir, name="creditoArchivos_subir"),
]

