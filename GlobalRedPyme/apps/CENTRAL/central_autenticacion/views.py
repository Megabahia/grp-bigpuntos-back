from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from apps.CENTRAL.central_usuarios.models import Usuarios
from apps.CENTRAL.central_usuarios.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login,logout,authenticate
# ObjectId
from bson import ObjectId
#token login
from rest_framework.authtoken.views import ObtainAuthToken
from apps.CENTRAL.central_autenticacion.models import Token
from apps.CENTRAL.central_autenticacion.auth import token_expire_handler,expires_in, deleteExpiredTokens
from django.utils import timezone
#logs
from apps.CENTRAL.central_logs.methods import createLog,datosAuth,datosTipoLog
#permisos
from apps.CENTRAL.central_roles.models import Roles
from apps.CENTRAL.central_acciones.models import Acciones, AccionesPermitidas, AccionesPorRol
#declaracion variables log
datosAux=datosAuth()
datosTipoLogAux=datosTipoLog()
#asignacion datos modulo
logModulo=datosAux['modulo']
logApi=datosAux['api']
#asignacion tipo de datos
logTransaccion=datosTipoLogAux['transaccion']
logExcepcion=datosTipoLogAux['excepcion']


class login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        #log
        timezone_now = timezone.localtime(timezone.now())
        logModel = {
            'endPoint': logApi+'login/',
            'modulo':logModulo,
            'tipo' : logExcepcion,
            'accion' : 'LEER',
            'fechaInicio' : str(timezone_now),
            'dataEnviada' : '{}',
            'fechaFin': str(timezone_now),
            'dataRecibida' : '{}'
        }
        try:
            logModel['dataEnviada'] = str(request.data)
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                if user.state==1:
                    token= Token.objects.create(user=user)
                    #ELIMINAR USUARIOS EXPIRADOS
                    deleteExpiredTokens()
                    #inner join para sacar los permisos urls
                    # acciones=AccionesPermitidas.objects.extra(tables=['central_acciones_acciones','central_acciones_accionesporrol'], 
                    # where=[
                        # 'central_acciones_acciones._id=central_acciones_accionespermitidas.idAccion_id',
                        # 'central_acciones_acciones.state=1',
                        # 'central_acciones_accionesporrol.idAccion_id=central_acciones_acciones._id',
                        # 'central_acciones_accionesporrol.idRol_id='+str(user.roles._id)
                    # ], select={'url': 'central_acciones_accionespermitidas.url'})
                    # acciones = cursor.execute('''db.central_acciones_acciones.find()''')
                    # acciones = AccionesPermitidas.objects.raw('db.central_acciones_accionespermitidas.find()')
                    # print(acciones)
                    data={
                        'token': token.key,
                        'id': str(user.pk),
                        'full_name': user.nombres+" "+user.apellidos,
                        'email': user.email,
                        'tokenExpiracion': expires_in(token),
                        'permisos':[]
                    }
                    # for accion in acciones:
                    #     data['permisos'].append({'url':str(accion)})
                    createLog(logModel,data,logTransaccion)
                    return Response(data,status=status.HTTP_200_OK)        
                else:
                    err={'error':'el usuario no existe!'}
                    createLog(logModel,err,logExcepcion)
                    return Response(err,status=status.HTTP_404_NOT_FOUND)  
            else:
                createLog(logModel,serializer.errors,logExcepcion)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST) 
            