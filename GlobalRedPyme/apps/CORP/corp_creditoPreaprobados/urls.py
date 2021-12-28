from django.urls import path,include
from apps.CORP.corp_creditoPreaprobados.views import(
	creditoPreaprobados_create,
	creditoPreaprobados_list,
	creditoPreaprobados_listOne,
	creditoPreaprobados_update,
	creditoPreaprobados_delete,
)
app_name = 'corp_creditoPreaprobados'

urlpatterns = [
	path('create/', creditoPreaprobados_create, name="creditoPreaprobados_create"),
	path('list/', creditoPreaprobados_list, name="creditoPreaprobados_list"),
	path('listOne/<str:pk>', creditoPreaprobados_listOne, name="creditoPreaprobados_listOne"),
	path('update/<str:pk>', creditoPreaprobados_update, name="creditoPreaprobados_update"),
	path('delete/<str:pk>', creditoPreaprobados_delete, name="creditoPreaprobados_delete"),
]

