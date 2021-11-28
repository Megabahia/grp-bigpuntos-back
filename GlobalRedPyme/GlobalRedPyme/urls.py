"""GlobalRedPyme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # PYMES
    path('pymes/empresas/', include(('apps.PYMES.pymes_empresas.urls', 'empresas'), namespace='empresas')),
    # CENTRAL
    path('core/monedas/', include(('apps.CORE.core_monedas.urls', 'monedas'), namespace='monedas')),
    #MODULO CENTRAL
    path('central/roles/', include(('apps.CENTRAL.central_roles.urls', 'roles'), namespace='roles')),
    path('central/usuarios/', include(('apps.CENTRAL.central_usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('central/auth/', include(('apps.CENTRAL.central_autenticacion.urls', 'autenticacion'), namespace='autenticacion')),
    path('central/acciones/', include(('apps.CENTRAL.central_acciones.urls', 'acciones'), namespace='acciones')),
    path('central/param/', include(('apps.CENTRAL.central_catalogo.urls', 'catalogo'), namespace='catalogo')),
    path('central/facturas/', include(('apps.CENTRAL.central_facturas.urls', 'facturas'), namespace='facturas')),
    url(r'^central/auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('central/productos/', include(('apps.CENTRAL.central_productos.urls', 'productos'), namespace='productos')),
    path('central/publicaciones/', include(('apps.CENTRAL.central_publicaciones.urls', 'publicaciones'), namespace='publicaciones')),
    # PERSONAS
    path('personas/personas/', include(('apps.PERSONAS.personas_personas.urls', 'personas'), namespace='personas')),
    path('personas/historialLaboral/', include(('apps.PERSONAS.personas_historialLaboral.urls', 'historialLaboral'), namespace='historialLaboral')),
    # CORP
    path('corp/cobrarSupermonedas/', include(('apps.CORP.corp_cobrarSupermonedas.urls', 'cobrarSupermonedas'), namespace='cobrarSupermonedas')),
    path('corp/autorizacion/', include(('apps.CORP.corp_autorizaciones.urls', 'autorizacion'), namespace='autorizacion')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

