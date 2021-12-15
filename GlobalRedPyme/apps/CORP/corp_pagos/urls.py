from django.urls import path,include
from apps.CORP.corp_pagos.views import(
	pagos_create,
	pagos_listOne,
	pagos_update,
	pagos_delete
)
app_name = 'corp_pagos'

urlpatterns = [
	path('create/', pagos_create, name="pagos_create"),
	path('listOne/<str:pk>', pagos_listOne, name="pagos_listOne"),
	path('update/<str:pk>', pagos_update, name="pagos_update"),
	path('delete/<str:pk>', pagos_delete, name="pagos_delete"),
]

