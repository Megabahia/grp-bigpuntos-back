from django.urls import path
from .views import (
    pagos_create,
    pagos_listOne,
    pagos_update,
    pagos_delete,
    pagos_list,
)

app_name = 'corp_pagos'

urlpatterns = [
    path('create/', pagos_create, name="pagos_create"),
    path('list/', pagos_list, name="pagos_list"),
    path('listOne/<str:pk>', pagos_listOne, name="pagos_listOne"),
    path('update/<str:pk>', pagos_update, name="pagos_update"),
    path('delete/<str:pk>', pagos_delete, name="pagos_delete"),
]
