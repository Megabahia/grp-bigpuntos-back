from .models import Monedas, Comisiones
from ...PERSONAS.personas_personas.models import Personas
from ...CORP.corp_empresas.models import Empresas
from .serializers import (
    MonedasSerializer, MonedasUsuarioSerializer, ListMonedasSerializer, ListMonedasRegaladasSerializer,
    ListComisionesSerializer
)
from .cron import hi
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
# Swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# ObjectId
from bson import ObjectId
# Utils
from apps.utils import utils

from ...PERSONAS.personas_personas.security import encriptar
from ...config import config
# IMPORTAR ENVIO CONFIGURACION CORREO
from apps.config.util2 import sendEmail
# excel
import openpyxl
# logs
from ...CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP

# declaracion variables log
datosAux = datosProductosMDP()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


# CRUD CORE
# LISTAR TODOS
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'],
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         required=['page_size', 'page'],
                         properties={
                             'page_size': openapi.Schema(type=openapi.TYPE_NUMBER),
                             'page': openapi.Schema(type=openapi.TYPE_NUMBER),
                             'user_id': openapi.Schema(type=openapi.TYPE_STRING),
                         },
                     ),
                     operation_description='Uninstall a version of Site',
                     responses={200: ListMonedasSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def monedas_list(request):
    """
    Este metodo se usa para listar las monedas por usuario de la tabla monedas de la base datos core
    @type request: El campo request recibe page, page_size, user_id
    @rtype: Devuelve una lista de las monedas de los usuario, caso contrario devuelve el error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'list/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            # paginacion
            page_size = int(request.data['page_size'])
            page = int(request.data['page'])
            offset = page_size * page
            limit = offset + page_size
            # Filtros
            filters = {"state": "1"}

            if 'user_id' in request.data and request.data['user_id'] != '':
                filters['user_id'] = request.data['user_id']

            # Serializar los datos
            query = Monedas.objects.filter(**filters).order_by('-created_at')
            serializer = ListMonedasSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


# CREAR
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=MonedasSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def monedas_create(request):
    """
    Este metodo se usa para crear las monedas de los usuario en la tabla monedas de la base datos core
    @type request: El campo request recibe los campo de la tabla monedas
    @rtype: Devuelve el registro que se crea, caso contrario devuelve el error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'create/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'CREAR',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            request.data['created_at'] = str(timezone_now)
            if 'updated_at' in request.data:
                request.data.pop('updated_at')

            serializer = MonedasSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ENCONTRAR UNO
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monedas_listOne(request, pk):
    """
    Este metodo se usa para listar un registro por el id en la tabla de monedas de la base datos core
    @type pk: El campo pk recibe el id del registro
    @type request: El campo request no recibe nada
    @rtype: Devuelve el registro que se busca, caso contrario devuelve
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'listOne/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        try:
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            query = Monedas.objects.get(pk=pk, state=1)
        except Monedas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'GET':
            serializer = MonedasSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ACTUALIZAR
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=MonedasSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def monedas_update(request, pk):
    """
    Este metodo se usa para actualizar registro por el id en la tabla de monedas de la base datos core
    @type pk: El campo pk recibe el id del registro
    @type request: El campo request recibe los campos de la tabla de monedas
    @rtype: Devuelve el registro que se actualiza, caso contrario devuelve error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'update/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'ESCRIBIR',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        try:
            logModel['dataEnviada'] = str(request.data)
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            query = Monedas.objects.get(pk=pk, state=1)
        except Monedas.DoesNotExist:
            errorNoExiste = {'error': 'No existe'}
            createLog(logModel, errorNoExiste, logExcepcion)
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            now = timezone.localtime(timezone.now())
            request.data['updated_at'] = str(now)
            if 'created_at' in request.data:
                request.data.pop('created_at')

            serializer = MonedasSerializer(query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# #ELIMINAR
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def monedas_delete(request, pk):
    """
    Este metodo se usa para borrar el registro de la moneda de la tabla monedas de la base datos core
    @type pk: el campo pk recibe el id del registro
    @type request: El campo request no recibe nada
    @rtype: Devuelve el registro eliminado,caso contrario devuelve el error generado
    """
    nowDate = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'delete/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'BORRAR',
        'fechaInicio': str(nowDate),
        'dataEnviada': '{}',
        'fechaFin': str(nowDate),
        'dataRecibida': '{}'
    }
    try:
        try:
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            persona = Monedas.objects.get(pk=pk, state=1)
        except Monedas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'DELETE':
            serializer = MonedasSerializer(persona, data={'state': '0', 'updated_at': str(nowDate)}, partial=True)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel, serializer.data, logTransaccion)
                return Response(serializer.data, status=status.HTTP_200_OK)
            createLog(logModel, serializer.errors, logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)

    # ENCONTRAR MONEDAS USUARIO


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monedas_usuario(request, pk):
    """
    este metodo obtine elultimo registro usuario en orden cronologico de la tabla de monedas de la base datos core
    @type pk: El campo pk recibe el user_id
    @type request: El campo request no recibe nada
    @rtype: Devuelve el ultimo registro de las monedas del usuario, caso contrario devuelve el error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'listOne/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        try:
            query = Monedas.objects.filter(user_id=pk, state=1).order_by('-created_at').first()
        except Monedas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'GET':
            serializer = MonedasUsuarioSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# LISTAR MONEDAS OTORGADAS POR COMPRA
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'],
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         required=['page_size', 'page'],
                         properties={
                             'page_size': openapi.Schema(type=openapi.TYPE_NUMBER),
                             'page': openapi.Schema(type=openapi.TYPE_NUMBER),
                             'user_id': openapi.Schema(type=openapi.TYPE_STRING),
                         },
                     ),
                     operation_description='Uninstall a version of Site',
                     responses={200: ListMonedasSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def monedas_listOtorgadas(request):
    """
    este metodo sirve para consultar la monedas otorgadas al usuario de la tabla monedas de la base datos core
    @type request: El campo request recibe el campo tipo, page, page_size, user_id
    @rtype: Devuelve una lista de los registros filtrados, caso contrario devuevle error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'list/otorgadas/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            # paginacion
            page_size = int(request.data['page_size'])
            page = int(request.data['page'])
            offset = page_size * page
            limit = offset + page_size
            # Filtros
            filters = {"state": "1"}
            filters['tipo__in'] = ['Credito', 'Otro']

            if 'user_id' in request.data:
                if request.data['user_id'] != '':
                    filters['user_id'] = request.data['user_id']

            # Serializar los datos
            query = Monedas.objects.filter(**filters).order_by('-created_at')
            serializer = ListMonedasSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


# METODO SUBIR ARCHIVOS EXCEL
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadEXCEL_monedasRegaladas(request):
    """
    Este metodo se usa para leer el excel para ingresar los registros en la tabla de monedas de base datos core
    @type request: El campo request recibe el archivo con los registros de las monedas regaladas
    @rtype: Devuelve una lista con los registros correctos, incorrectos, caso contrario devuelve el error generado
    """
    contValidos = 0
    contInvalidos = 0
    contTotal = 0
    errores = []
    try:
        if request.method == 'POST':
            first = True  # si tiene encabezado
            uploaded_file = request.FILES['documento']
            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(uploaded_file)
            # getting a particular sheet by name out of many sheets
            worksheet = wb["Clientes"]
            lines = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            lines.append(row_data)

        for dato in lines:
            contTotal += 1
            if first:
                first = False
                continue
            else:
                if len(dato) == 9:
                    resultadoInsertar = insertarDato_creditoPreaprobado(dato)
                    if resultadoInsertar != 'Dato insertado correctamente':
                        contInvalidos += 1
                        errores.append({"error": "Error en la línea " + str(contTotal) + ": " + str(resultadoInsertar)})
                    else:
                        contValidos += 1
                else:
                    contInvalidos += 1
                    errores.append({"error": "Error en la línea " + str(
                        contTotal) + ": la fila tiene un tamaño incorrecto (" + str(len(dato)) + ")"})

        result = {"mensaje": "La Importación se Realizo Correctamente",
                  "correctos": contValidos,
                  "incorrectos": contInvalidos,
                  "errores": errores
                  }
        return Response(result, status=status.HTTP_201_CREATED)

    except Exception as e:
        err = {"error": 'Error verifique el archivo, un error ha ocurrido: {}'.format(e)}
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# INSERTAR DATOS EN LA BASE INDIVIDUAL
def insertarDato_creditoPreaprobado(dato):
    """
    este metodo se ingresa en la tabla de monedas
    @type dato: El campo dato recibe la fila del excel
    @rtype: Devuelve el estado correcto, caso contrario los errores generados
    """
    try:
        timezone_now = timezone.localtime(timezone.now())
        if (not utils.__validar_ced_ruc(dato[0], 0)):
            return 'Cedula incorrecta'
        data = {}
        hash_identificacion = encriptar(dato[0])
        persona = Personas.objects.filter(identificacion=hash_identificacion, state=1).first()
        if persona is not None:
            data['user_id'] = persona.user_id
        empresa = Empresas.objects.filter(ruc=dato[4], state=1).first()
        if empresa is None:
            return 'El ruc de la empresa no esta registrada'
        data['identificacion'] = dato[0]
        data['nombres'] = dato[1]
        data['apellidos'] = dato[2]
        data['email'] = dato[3]
        data['empresa_id'] = empresa._id
        data['tipo'] = 'Otro'
        data['estado'] = 'pendiente'
        data['credito'] = dato[6].replace('"', "") if dato[6] != "NULL" else None
        if persona is not None:
            monedasUsuario = Monedas.objects.filter(user_id=persona.user_id, state=1).order_by(
                '-created_at').first().saldo
        else:
            monedasUsuario = 0
        data['saldo'] = monedasUsuario + float(dato[6])
        data['descripcion'] = dato[8].replace('"', "") if dato[8] != "NULL" else None
        # data['fechaVigencia'] = dato[8].replace('"', "")[0:10] if dato[8] != "NULL" else None
        data['created_at'] = str(timezone_now)
        # inserto el dato con los campos requeridos
        Monedas.objects.create(**data)
        enviarCorreoSolicitud(data['email'], data['credito'])
        return 'Dato insertado correctamente'
    except Exception as e:
        return str(e)


def enviarCorreoSolicitud(email, monedas):
    """
    Este metodo realiza el envio de la estructura del email
    @type monedas: El campo monedas recibe la cantidad de monedas que se regalaran
    @type email: El campo email recibe el email del cliente al cual se le regalara las monedas
    @rtype: No devuelve nada
    """
    subject, from_email, to = 'RECOMPENSA BIG PUNTOS', "credicompra.bigpuntos@corporacionomniglobal.com", \
                              email
    txt_content = f"""
                        ¡FELICIDADES!
                        USTED ACABA DE RECIBIR {monedas} para que realice compras en los establecimientos 
                        afiliados pagando menos dinero en efectivo
                        Regístrese a través de nuestro portal {config.API_FRONT_END_CENTRAL} y reciba sus
                        Big Puntos de recompensa en su cuenta
                        Atentamente,
                        CrediCompra - Big Puntos
    """
    html_content = f"""
                <html>
                    <body>
                        <h1>¡FELICIDADES!</h1>
                        <br>
                        <p>USTED ACABA DE RECIBIR <b>{monedas}</b> para que realice compras en los establecimientos 
                        afiliados pagando menos dinero en efectivo</p>
                        <br>
                        <br>
                        <p>Regístrese a través de nuestro portal {config.API_FRONT_END_CENTRAL} y reciba sus
                        Big Puntos de recompensa en su cuenta</p>
                        <br>
                        <br>
                        Atentamente,
                        <br>
                        CrediCompra - Big Puntos
                        <br>
                    </body>
                </html>
                """
    sendEmail(subject, txt_content, from_email, to, html_content)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_monedas_regaladas_empresa(request):
    """
    Este metodo lista las monedas regaladas que estan en la tabla monedas de la base datos core
    @type request: El campo request recibe page, page_size, user_id
    @rtype: Devuelve una lista de las monedas que se regalaron
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'list/otorgadas/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            # paginacion
            page_size = int(request.data['page_size'])
            page = int(request.data['page'])
            offset = page_size * page
            limit = offset + page_size
            # Filtros
            filters = {"state": "1"}
            filters['fechaVigencia__isnull'] = False
            # filters['fechaVigencia__gte'] = str(timezone_now)[0:10]

            if 'user_id' in request.data:
                if request.data['user_id'] != '':
                    filters['user_id'] = request.data['user_id']

            # Serializar los datos
            query = Monedas.objects.filter(**filters).order_by('-created_at')
            serializer = ListMonedasRegaladasSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pruebaConsumer(request):
    """
    Este metodo se usa para consumir la cola de aws, para que el usuario no tenga que esperar
    @rtype: Devuelve el estado actualizado, caso contrario devuelve el error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'consumer/AWS',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        hi()
        msg = {"msg": "Se actualizo la cola"}
        return Response(msg, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comiciones_list(request):
    """
    Este metodo se usa para listar las monedas por usuario de la tabla monedas de la base datos core
    @type request: El campo request recibe page, page_size, user_id
    @rtype: Devuelve una lista de las monedas de los usuario, caso contrario devuelve el error generado
    """
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi + 'list/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'LEER',
        'fechaInicio': str(timezone_now),
        'dataEnviada': '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            # paginacion
            page_size = int(request.data['page_size'])
            page = int(request.data['page'])
            offset = page_size * page
            limit = offset + page_size
            # Filtros
            filters = {"state": "1"}

            if 'user_id' in request.data and request.data['user_id'] != '':
                filters['user_id'] = request.data['user_id']

            if 'identificacion' in request.data and request.data['identificacion'] != '':
                filters['identificacion'] = request.data['identificacion']

            # Serializar los datos
            query = Comisiones.objects.filter(**filters).order_by('-created_at')
            serializer = ListComisionesSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)