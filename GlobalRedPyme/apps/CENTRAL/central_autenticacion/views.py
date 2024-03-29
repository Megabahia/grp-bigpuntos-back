from django_rest_passwordreset.views import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..central_usuarios.models import Usuarios, UsuariosEmpresas
from ...CORP.corp_creditoPersonas.models import CreditoPersonas
# Importar base de datos personas
from ...PERSONAS.personas_personas.models import Personas
# Importar serializers empresa y base de datos empresa
from ...CORP.corp_empresas.models import Empresas
from ...CORP.corp_empresas.serializers import EmpresasSerializer
# Importar serializer de personas
from ...PERSONAS.personas_personas.serializers import PersonasSerializer
# ObjectId
from bson import ObjectId
# token login
from ...CENTRAL.central_autenticacion.models import Token
from ...CENTRAL.central_autenticacion.auth import token_expire_handler, expires_in, deleteExpiredTokens
from django.utils import timezone
# logs
from ...CENTRAL.central_logs.methods import createLog, datosAuth, datosTipoLog
# permisos
from ...CENTRAL.central_roles.models import RolesUsuarios
from ...CENTRAL.central_roles.serializers import ListRolesSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# declaracion variables log
datosAux = datosAuth()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


class login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # log
        timezone_now = timezone.localtime(timezone.now())
        logModel = {
            'endPoint': logApi + 'login/',
            'modulo': logModulo,
            'tipo': logExcepcion,
            'accion': 'LEER',
            'fechaInicio': str(timezone_now),
            'dataEnviada': '{}',
            'fechaFin': str(timezone_now),
            'dataRecibida': '{}'
        }
        try:
            logModel['dataEnviada'] = str(request.data)
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                if user.state == 1:
                    if user.estado == "1":
                        data = {
                            'code': 400,
                            'msg': 'Por favor confirmar su correo electrónico, el Link fué enviado a la cuenta de correo electrónico registrado, si no recuerda usar por favor la Opción ¿Olvidaste tu contraseña?.'
                        }
                        return Response(data, status=status.HTTP_200_OK)
                    if user.tipoUsuario.nombre != request.data['tipoUsuario']:
                        data = {'error': 'Usted no tiene una cuenta.'}
                        return Response(data, status=status.HTTP_404_NOT_FOUND)
                    token = Token.objects.create(user=user)
                    # ELIMINAR USUARIOS EXPIRADOS
                    deleteExpiredTokens()
                    # Consultar roles de usuario
                    rolesUsuario = RolesUsuarios.objects.filter(usuario=user, state=1)
                    roles = ListRolesSerializer(rolesUsuario, many=True).data
                    # Consultar datos de la persona en GRP_PERSONAS_PERSONAS
                    try:
                        persona = Personas.objects.get(user_id=user._id)
                        personaSerializer = PersonasSerializer(persona).data
                    except Exception as e:
                        personaSerializer = {}

                    try:
                        empresa = UsuariosEmpresas.objects.filter(usuario=user).first()
                        empresaSerializer = EmpresasSerializer(
                            Empresas.objects.filter(_id=ObjectId(empresa.empresa_id)).first()).data
                    except Exception as e:
                        empresaSerializer = {}
                    try:
                        credito = True if CreditoPersonas.objects.filter(user_id=user._id,
                                                              estado__in=['Nuevo', 'Enviado', 'Por Completar']
                                                              ) else False

                    except Exception as e:
                        personaSerializer = {}

                    data = {
                        'token': token.key,
                        'id': str(user.pk),
                        'persona': personaSerializer,
                        'empresa': empresaSerializer,
                        'email': user.email,
                        'tokenExpiracion': expires_in(token),
                        'roles': roles,
                        'estado': user.estado,
                        'noPuedeSolicitar': credito
                    }
                    createLog(logModel, data, logTransaccion)
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    err = {'error': 'el usuario no existe!'}
                    createLog(logModel, err, logExcepcion)
                    return Response(err, status=status.HTTP_404_NOT_FOUND)
            else:
                createLog(logModel, serializer.errors, logExcepcion)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginFacebookView(request):
    if request.method == 'POST':
        try:
            emailUser = request.data['username']
            user = User.objects.get(email__exact=emailUser)
            token = Token.objects.create(user=user)
            # user.token = token
            rolesUsuario = RolesUsuarios.objects.filter(usuario=user, state=1)
            roles = ListRolesSerializer(rolesUsuario, many=True).data
            try:
                persona = Personas.objects.get(user_id=user._id)
                personaSerializer = PersonasSerializer(persona).data
            except Exception as e:
                personaSerializer = {}

            try:
                empresa = UsuariosEmpresas.objects.filter(usuario=user).first()
                empresaSerializer = EmpresasSerializer(
                    Empresas.objects.filter(_id=ObjectId(empresa.empresa_id)).first()).data
            except Exception as e:
                empresaSerializer = {}

            data = {
                'token': token.key,
                'id': str(user.pk),
                'persona': personaSerializer,
                'empresa': empresaSerializer,
                'email': user.email,
                'tokenExpiracion': expires_in(token),
                'roles': roles,
                'estado': user.estado
            }
            print('data', data)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)
