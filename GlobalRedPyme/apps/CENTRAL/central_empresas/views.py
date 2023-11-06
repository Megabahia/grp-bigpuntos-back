"""Nube Bigpuntos
PORTALES: CENTER, PERSONAS, CORP, IFIS
"""

from apps.config import config
from .models import Empresas
from .serializers import (
    EmpresasSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
# ObjectId
from bson import ObjectId
# logs
from apps.CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP

# declaracion variables log
datosAux = datosProductosMDP()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


# CRUD
# LISTAR TODOS
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def empresas_list(request):
    """
    Esta metodo se usa para listar las empresas segun los filtros de la tabla de empresas, de la base datos central
    @type request: El campo request recibe nombreComercial, tipoEmpresa, page, page_size
    @rtype: Devuelve una lista de las empresas con los filtros aplicados, caso contrario devuelve un error
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

            if "nombreComercial" in request.data:
                if request.data["nombreComercial"] != '':
                    filters['nombreComercial__icontains'] = str(request.data["nombreComercial"])

            if "tipoEmpresa" in request.data:
                if request.data["tipoEmpresa"] != '':
                    filters['tipoEmpresa'] = str(request.data["tipoEmpresa"])

            # Serializar los datos
            query = Empresas.objects.filter(**filters).order_by('-created_at')
            serializer = EmpresasSerializer(query[offset:limit], many=True)
            new_serializer_data = {'cont': query.count(),
                                   'info': serializer.data}
            # envio de datos
            return Response(new_serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            err = {"error": 'Un error ha ocurrido: {}'.format(e)}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


# CREAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def empresas_create(request):
    """
    Este metodo se usa para guardar una empresa en la tabla de empresas, de la base datos central
    @type request: El campo request recibe los parametros de la tabla de empresas
    @rtype: Devuelve el registro que se acaba de registrar, caso contrario devuelve los errores generados
    """
    request.POST._mutable = True
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
            filters = {'estado': 'Activo', 'state': 1}

            if 'type' in request.data:
                if request.data['type'] != '':
                    filters['type'] = request.data['type']

            if 'nombre' in request.data:
                if request.data['nombre'] != '':
                    filters['nombre'] = request.data['nombre']

            empresa = Empresas.objects.filter(**filters).first()
            if empresa is not None:
                data = {'error': 'El nombre ya esta registrado.'}
                createLog(logModel, data, logExcepcion)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if request.data['type'] == 'cliente':
                request.data['urlClientes'] = config.API_FRONT_END_CENTRAL + '/pages/clientes/' + request.data[
                    'nombre'].replace(" ",
                                      "-")

                empresa = Empresas.objects.filter(urlClientes=request.data['urlClientes'], estado='Activo',
                                                  state=1).first()
                if empresa is not None:
                    data = {'error': 'La url ya esta registrado.'}
                    createLog(logModel, data, logExcepcion)
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if request.data['type'] == 'empleado':
                request.data['url'] = config.API_FRONT_END_CENTRAL + '/pages/socios-empleados/' + request.data[
                    'nombre'].replace(" ",
                                      "-")

                empresa = Empresas.objects.filter(url=request.data['url'], estado='Activo', state=1).first()
                if empresa is not None:
                    data = {'error': 'La url ya esta registrado.'}
                    createLog(logModel, data, logExcepcion)
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)

            serializer = EmpresasSerializer(data=request.data)
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
def empresas_listOne(request, pk):
    """
    Este metodo se usa para listar una empresa por el id de la tabla de empresas de la base de datos central
    @type pk: El campo pk es el id
    @type request: No recibe datos por el request
    @rtype: Devuelve una empresa si encuentra, caso contrario devuelve error
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
            query = Empresas.objects.get(pk=pk, state=1)
        except Empresas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'GET':
            serializer = EmpresasSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ENCONTRAR UNO
@api_view(['GET'])
def empresas_listOne_url(request, pk):
    """
    Este metodo consulta por la url a la tabla de la empresa de la base de datos central
    @type pk: En la pk recibe el id de la empresa
    @type request: No recibe nada en el request
    @rtype: Devuelve la empresa que coincide con la url caso contrario devuelve error
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
            url = config.API_FRONT_END_CENTRAL + '/pages/socios-empleados/' + pk
            query = Empresas.objects.get(url=url, state=1)
        except Empresas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_200_OK)
        # tomar el dato
        if request.method == 'GET':
            serializer = EmpresasSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ENCONTRAR UNO
@api_view(['GET'])
def empresas_listOne_url_clientes(request, pk):
    """
    Este metodo consulta por url para las empresas que los clientes puedan visualizar la informacion de la empresa
    de la tabla de empresa de la base de datos central
    @type pk: El campo pk recibe el id de la empresa que desea consultar
    @type request: No recibe nada el campo request
    @rtype: DEvuelve la empresa que coincida con la url, caso contrario devuelve un error
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
            url = config.API_FRONT_END_CENTRAL + '/pages/clientes/' + pk
            query = Empresas.objects.get(urlClientes=url, state=1)
        except Empresas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_200_OK)
        # tomar el dato
        if request.method == 'GET':
            serializer = EmpresasSerializer(query)
            createLog(logModel, serializer.data, logTransaccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


# ACTUALIZAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def empresas_update(request, pk):
    """
    Este metodo permite actualizar las empresas de la tabla empresas de la base de datos central
    @type pk: El campo pk recibe el id
    @type request: El campo request recibe los datos de la tabla empresa
    @rtype: devuelve el registro actualizado, caso contrario devuelve los error que tenga el registro
    """
    request.POST._mutable = True
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
            query = Empresas.objects.get(pk=pk, state=1)
        except Empresas.DoesNotExist:
            errorNoExiste = {'error': 'No existe'}
            createLog(logModel, errorNoExiste, logExcepcion)
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            now = timezone.localtime(timezone.now())
            request.data['updated_at'] = str(now)
            if 'created_at' in request.data:
                request.data.pop('updated_at')

            filters = {'estado': 'Activo', 'state': 1}

            if 'type' in request.data:
                if request.data['type'] != '':
                    filters['type'] = request.data['type']

            if 'nombre' in request.data:
                if request.data['nombre'] != '':
                    filters['nombre'] = request.data['nombre']

            empresa = Empresas.objects.filter(**filters).exclude(_id=pk).first()
            if empresa is not None:
                data = {'error': 'El nombre ya esta registrado.'}
                createLog(logModel, data, logExcepcion)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if request.data['type'] == 'cliente':
                request.data['urlClientes'] = config.API_FRONT_END_CENTRAL + '/pages/clientes/' + request.data[
                    'nombre'].replace(" ",
                                      "-")

                empresa = Empresas.objects.filter(urlClientes=request.data['urlClientes'], estado='Activo',
                                                  state=1).exclude(_id=pk).first()
                if empresa is not None:
                    data = {'error': 'La url ya esta registrado.'}
                    createLog(logModel, data, logExcepcion)
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if request.data['type'] == 'empleado':
                request.data['url'] = config.API_FRONT_END_CENTRAL + '/pages/socios-empleados/' + request.data[
                    'nombre'].replace(" ",
                                      "-")

                empresa = Empresas.objects.filter(url=request.data['url'], estado='Activo', state=1).exclude(
                    _id=pk).first()
                if empresa is not None:
                    data = {'error': 'La url ya esta registrado.'}
                    createLog(logModel, data, logExcepcion)
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)

            serializer = EmpresasSerializer(query, data=request.data, partial=True)
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


# ELIMINAR
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def empresas_delete(request, pk):
    """
    Este metodo elimina la empresa de la tabla empresa de la base de datos central
    @type pk: El campo pk recibe el id de la empresa que se desea eliminar
    @type request: El campo request no recibe nada
    @rtype: Devuelve el registro eliminado, caso contrario devuelve el error que se produzca
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
            persona = Empresas.objects.get(pk=pk, state=1)
        except Empresas.DoesNotExist:
            err = {"error": "No existe"}
            createLog(logModel, err, logExcepcion)
            return Response(err, status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        # tomar el dato
        if request.method == 'DELETE':
            serializer = EmpresasSerializer(persona, data={'state': '0', 'updated_at': str(nowDate)}, partial=True)
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
