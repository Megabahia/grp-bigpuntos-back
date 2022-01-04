from apps.CORP.corp_creditoPreaprobados.models import  CreditoPreaprobados
from apps.PERSONAS.personas_personas.models import  Personas
from django.db.models import Q
from apps.CORP.corp_creditoPreaprobados.serializers import (
    CreditoPreaprobadosSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
# Swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# ObjectId
from bson import ObjectId
#logs
from apps.CENTRAL.central_logs.methods import createLog,datosTipoLog, datosProductosMDP
#declaracion variables log
datosAux=datosProductosMDP()
datosTipoLogAux=datosTipoLog()
#asignacion datos modulo
logModulo=datosAux['modulo']
logApi=datosAux['api']
#asignacion tipo de datos
logTransaccion=datosTipoLogAux['transaccion']
logExcepcion=datosTipoLogAux['excepcion']
#CRUD PERSONAS
#LISTAR TODOS
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'],
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['page_size','page'],
                             properties={
                                 'page_size': openapi.Schema(type=openapi.TYPE_NUMBER),
                                 'page': openapi.Schema(type=openapi.TYPE_NUMBER)
                             },
                         ),
                         operation_description='Uninstall a version of Site',
                         responses={200: CreditoPreaprobadosSerializer(many=True)})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_list(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'list/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'LEER',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            #paginacion
            page_size=int(request.data['page_size'])
            page=int(request.data['page'])
            offset = page_size* page
            limit = offset + page_size
            #Filtros
            filters={"state":"1"}
        
            if "user_id" in request.data:
                if request.data["user_id"] != '':
                    filters['user_id'] = str(request.data["user_id"])
            if "tipoPersona" in request.data:
                if request.data["tipoPersona"] != '':
                    filters['tipoPersona'] = str(request.data["tipoPersona"])

            #Serializar los datos
            query = CreditoPreaprobados.objects.filter(**filters).order_by('-created_at')
            serializer = CreditoPreaprobadosSerializer(query[offset:limit], many=True)
            new_serializer_data={'cont': query.count(),
            'info':serializer.data}
            #envio de datos
            return Response(new_serializer_data,status=status.HTTP_200_OK)
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


#CREAR
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=CreditoPreaprobadosSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_create(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'create/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'CREAR',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            request.data['created_at'] = str(timezone_now)
            if 'updated_at' in request.data:
                request.data.pop('updated_at')
            
            request.data['empresa'] = ObjectId(request.data['empresa'])

            serializer = CreditoPreaprobadosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel,serializer.data,logTransaccion)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            createLog(logModel,serializer.errors,logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

#ENCONTRAR UNO
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_listOne(request, pk):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'listOne/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'LEER',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    try:
        try:
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            query = CreditoPreaprobados.objects.get(pk=pk, state=1)
        except CreditoPreaprobados.DoesNotExist:
            err={"error":"No existe"}  
            createLog(logModel,err,logExcepcion)
            return Response(err,status=status.HTTP_404_NOT_FOUND)
        #tomar el dato
        if request.method == 'GET':
            serializer = CreditoPreaprobadosSerializer(query)
            createLog(logModel,serializer.data,logTransaccion)
            return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

# ACTUALIZAR
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=CreditoPreaprobadosSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_update(request, pk):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'update/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'ESCRIBIR',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    try:
        try:
            logModel['dataEnviada'] = str(request.data)
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            query = CreditoPreaprobados.objects.get(pk=pk, state=1)
        except CreditoPreaprobados.DoesNotExist:
            errorNoExiste={'error':'No existe'}
            createLog(logModel,errorNoExiste,logExcepcion)
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            now = timezone.localtime(timezone.now())
            request.data['updated_at'] = str(now)
            if 'created_at' in request.data:
                request.data.pop('created_at')

            request.data['empresa_financiera'] = ObjectId(request.data['empresa_financiera'])
            
            if query.estado == 'Aprobado':
                serializer = CreditoPreaprobadosSerializer(query)
                createLog(logModel,serializer.data,logTransaccion)
                return Response(serializer.data)
            
            serializer = CreditoPreaprobadosSerializer(query, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel,serializer.data,logTransaccion)
                return Response(serializer.data)
            createLog(logModel,serializer.errors,logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e: 
        err={"error":'Un error ha ocurrido: {}'.format(e)}  
        createLog(logModel,err,logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST) 

#ELIMINAR
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_delete(request, pk):
    nowDate = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'delete/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'BORRAR',
        'fechaInicio' : str(nowDate),
        'dataEnviada' : '{}',
        'fechaFin': str(nowDate),
        'dataRecibida' : '{}'
    }
    try:
        try:
            # Creo un ObjectoId porque la primaryKey de mongo es ObjectId
            pk = ObjectId(pk)
            persona = CreditoPreaprobados.objects.get(pk=pk, state=1)
        except CreditoPreaprobados.DoesNotExist:
            err={"error":"No existe"}  
            createLog(logModel,err,logExcepcion)
            return Response(err,status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        #tomar el dato
        if request.method == 'DELETE':
            serializer = CreditoPreaprobadosSerializer(persona, data={'state': '0','updated_at':str(nowDate)},partial=True)
            if serializer.is_valid():
                serializer.save()
                createLog(logModel,serializer.data,logTransaccion)
                return Response(serializer.data,status=status.HTTP_200_OK)
            createLog(logModel,serializer.errors,logExcepcion)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e: 
        err={"error":'Un error ha ocurrido: {}'.format(e)}  
        createLog(logModel,err,logExcepcion)
        return Response(err, status=status.HTTP_400_BAD_REQUEST) 



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creditoPreaprobados_list_corp(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'list/corp/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'LEER',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    if request.method == 'POST':
        try:
            logModel['dataEnviada'] = str(request.data)
            #paginacion
            page_size=int(request.data['page_size'])
            page=int(request.data['page'])
            offset = page_size* page
            limit = offset + page_size
            #Filtros
            filters={"state":"1"}
        
            if "empresa_financiera" in request.data:
                if request.data["empresa_financiera"] != '':
                    filters['empresa_financiera'] = ObjectId(request.data["empresa_financiera"])
            if "tipoPersona" in request.data:
                if request.data["tipoPersona"] != '':
                    filters['tipoPersona'] = str(request.data["tipoPersona"])
            
            if "cedula" in request.data:
                if request.data["cedula"] != '':
                    cedulas = Personas.objects.filter(identificacion__icontains=str(request.data["cedula"]),state=1).values_list('user_id',flat=True)
                    arr = []
                    for id in cedulas:
                        arr.append(str(id))
                    filters['user_id__in'] = arr
                    
            if "nombresCompleto" in request.data:
                if request.data["nombresCompleto"] != '':
                    cedulas = Personas.objects.filter(Q(nombresCompleto__icontains=str(request.data["nombresCompleto"])),state=1).values_list('user_id',flat=True).distinct()
                    arr = []
                    print('holiiii')
                    for id in cedulas:
                        arr.append(str(id))
                    filters['user_id__in'] = arr

            #Serializar los datos
            query = CreditoPreaprobados.objects.filter(**filters).order_by('-created_at')
            serializer = CreditoPreaprobadosSerializer(query[offset:limit], many=True)
            new_serializer_data={'cont': query.count(),
            'info':serializer.data}
            #envio de datos
            return Response(new_serializer_data,status=status.HTTP_200_OK)
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)



