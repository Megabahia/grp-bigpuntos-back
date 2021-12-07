from django.urls import path,include
from apps.CORP.corp_empresas.views import(
	empresas_create,
	empresas_list,
	empresas_listOne,
	empresas_update,
	empresas_delete,
	empresas_list_filtro,
)
app_name = 'corp_empresas'

urlpatterns = [
	path('create/', empresas_create, name="empresas_create"),
	path('list/', empresas_list, name="empresas_list"),
	path('list/filtro', empresas_list_filtro, name="empresas_list_filtro"),
	path('listOne/<str:pk>', empresas_listOne, name="empresas_listOne"),
	path('update/<str:pk>', empresas_update, name="empresas_update"),
	path('delete/<str:pk>', empresas_delete, name="empresas_delete"),
]

