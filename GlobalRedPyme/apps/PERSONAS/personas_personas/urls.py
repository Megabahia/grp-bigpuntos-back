from django.urls import path,include
from apps.PERSONAS.personas_personas.views import(
	personas_create,
	personas_listOne,
	personas_update,
	personas_delete,
	# productos_findOne
)
app_name = 'personas'

urlpatterns = [
	path('create/', personas_create, name="personas_create"),
	path('listOne/<str:pk>', personas_listOne, name="personas_listOne"),
	path('update/<str:pk>', personas_update, name="personas_update"),
	path('delete/<str:pk>', personas_delete, name="personas_delete"),
	# path('list/', productos_findOne, name="productos_findOne"),
]

