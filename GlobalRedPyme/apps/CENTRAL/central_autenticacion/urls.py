from django.urls import path,include
from apps.CENTRAL.central_autenticacion.views import(
	login,
)
from .views import loginFacebookView

app_name = 'autenticacion'

urlpatterns = [
	path('login/', login.as_view(), name="login"), # -> see accounts/api/views.py for response and url info
	path('loginFacebook/', loginFacebookView, name="loginFacebook"), # -> see accounts/api/views.py for response and url info
]

