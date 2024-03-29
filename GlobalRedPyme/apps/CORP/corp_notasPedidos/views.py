from apps.PERSONAS.personas_personas.models import Personas
from apps.CENTRAL.central_catalogo.models import  Catalogo
from apps.CORP.corp_empresas.models import  Empresas
from apps.CORP.corp_creditoPersonas.models import  AutorizacionCredito
from apps.CORP.corp_notasPedidos.models import FacturasEncabezados, FacturasDetalles
from apps.CORP.corp_notasPedidos.serializers import FacturasSerializer, FacturasDetallesSerializer, FacturasListarSerializer, FacturaSerializer, FacturasListarTablaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime
from django.core import serializers
# Enviar Correo
from apps.config.util import sendEmail
# TWILIO
from twilio.rest import Client
from django.conf import settings
# Generar codigos aleatorios
import string
import random
#excel
import openpyxl
# ObjectId
from bson import ObjectId
#logs
from apps.CENTRAL.central_logs.methods import createLog,datosTipoLog, datosFacturas
#declaracion variables log
datosAux=datosFacturas()
datosTipoLogAux=datosTipoLog()
#asignacion datos modulo
logModulo=datosAux['modulo']
logApi=datosAux['api']
#asignacion tipo de datos
logTransaccion=datosTipoLogAux['transaccion']
logExcepcion=datosTipoLogAux['excepcion']
#CRUD PROSPECTO CLIENTES
#LISTAR TODOS
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def factura_list(request):
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

            if 'identificacion' in request.data:
                if 'identificacion' != '':
                    filters['identificacion__icontains'] = request.data['identificacion']
            
            if 'razonSocial' in request.data:
                if 'razonSocial' != '':
                    filters['razonSocial__icontains'] = request.data['razonSocial']
          
            #Serializar los datos
            query = FacturasEncabezados.objects.filter(**filters).order_by('-created_at')
            serializer = FacturasListarSerializer(query[offset:limit], many=True)
            new_serializer_data={'cont': query.count(),
            'info':serializer.data}
            #envio de datos
            return Response(new_serializer_data,status=status.HTTP_200_OK)
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST) 

#ENCONTRAR UNO
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def factura_findOne(request, pk):
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
            query = FacturasEncabezados.objects.get(pk=pk, state=1)
        except FacturasEncabezados.DoesNotExist:
            err={"error":"No existe"}  
            createLog(logModel,err,logExcepcion)
            return Response(err,status=status.HTTP_404_NOT_FOUND)
        #tomar el dato
        if request.method == 'GET':
            serializer = FacturasSerializer(query)
            createLog(logModel,serializer.data,logTransaccion)
            return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

#ENCONTRAR LA ULTIMA FACTURA
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def factura_list_latest(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'listLatest/',
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
            filters={"state":"1"}  
            if 'negocio' in request.data:                
                if request.data['negocio'] !='':   
                    filters['negocio__isnull'] = False

            if 'cliente' in request.data:                
                if request.data['cliente'] !='':   
                    filters['cliente__isnull'] = False
            
            query = FacturasEncabezados.objects.filter(**filters).order_by('-id')[0]
        except FacturasEncabezados.DoesNotExist:
            err={"error":"No existe"}  
            createLog(logModel,err,logExcepcion)
            return Response(err,status=status.HTTP_404_NOT_FOUND)
        #tomar el dato
        if request.method == 'GET':
            serializer = FacturasListarSerializer(query)
            createLog(logModel,serializer.data,logTransaccion)
            return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

#CREAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def factura_create(request):
    request.POST._mutable = True
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

            request.data['empresaComercial'] = ObjectId(request.data['empresaComercial'])
            request.data['credito'] = request.data['credito']
        
            serializer = FacturaSerializer(data=request.data)
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

# ACTUALIZAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def factura_update(request, pk):
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
            query = FacturasEncabezados.objects.get(pk=pk, state=1)
        except FacturasEncabezados.DoesNotExist:
            errorNoExiste={'error':'No existe'}
            createLog(logModel,errorNoExiste,logExcepcion)
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            now = timezone.localtime(timezone.now())
            request.data['updated_at'] = str(now)
            if 'created_at' in request.data:
                request.data.pop('created_at')

            request.data['empresaComercial'] = ObjectId(request.data['empresaComercial'])
            request.data['credito'] = request.data['credito']

            serializer = FacturasSerializer(query, data=request.data,partial=True)
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

#ENCONTRAR UNO
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def factura_findOne_credito(request, pk):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'listOne/credito/',
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
            pk = ObjectId(pk)
            query = FacturasEncabezados.objects.get(credito=pk, state=1)
        except FacturasEncabezados.DoesNotExist:
            err={"error":"No existe"}  
            createLog(logModel,err,logExcepcion)
            return Response(err,status=status.HTTP_404_NOT_FOUND)
        #tomar el dato
        if request.method == 'GET':
            serializer = FacturasSerializer(query)
            createLog(logModel,serializer.data,logTransaccion)
            return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST)


#GENERAR CODIGOS ENVIAR
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def factura_generar_codigos_envios(request):
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'generar/habilitantes/credito/',
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
            # Buscar informacion de la persona y empresa corp
            persona = Personas.objects.filter(user_id=request.data['user_id'],state=1).first()
            empresa = Empresas.objects.filter(pk=ObjectId(request.data['empresaComercial_id']),state=1).first()
            # Genera el codigo
            longitud_codigo = Catalogo.objects.filter(tipo='CONFIG_TWILIO',nombre='LONGITUD_CODIGO',state=1).first().valor
            numeroTwilio = Catalogo.objects.filter(tipo='CONFIG_TWILIO',nombre='NUMERO_TWILIO',state=1).first().valor
            codigoUsuario = (''.join(random.choice(string.digits) for _ in range(int(longitud_codigo))))
            codigoCorp = (''.join(random.choice(string.digits) for _ in range(int(longitud_codigo))))
            # Correo de cliente
            subject, from_email, to = 'Generacion de numero de autorización del cliente', "credicompra.bigpuntos@corporacionomniglobal.com",persona.email
            txt_content="""
                    Se acaba de generar el codigo de autorizacion del crédito
                    Comuniquese con su asesor del credito, el codigo de autorización es """+codigoUsuario+"""
                    Atentamente,
                    Equipo Global Red Pymes Personas.
            """
            html_content = """
            <html>
                <body>
                    <h1>Se acaba de generar el codigo de autorizacion del crédito</h1>
                    Comuniquese con su asesor del credito, el codigo de autorización es """+codigoUsuario+"""<br>
                    Atentamente,<br>
                    Equipo Global Red Pymes Personas.<br>
                </body>
            </html>
            """
            sendEmail(subject, txt_content, from_email,to,html_content)
            # Correo de la corp
            subject, from_email, to = 'Generacion de numero de autorización de la empresa CORP', "credicompra.bigpuntos@corporacionomniglobal.com",empresa.correo
            txt_content="""
                    Se acaba de generar el codigo de autorizacion del crédito
                    Comuniquese con su asesor del credito, el codigo de autorización es """+codigoCorp+"""
                    Atentamente,
                    Equipo Global Red Pymes Personas.
            """
            html_content = """
            <html>
                <body>
                    <h1>Se acaba de generar el codigo de autorizacion del crédito</h1>
                    Comuniquese con su asesor del credito, el codigo de autorización es """+codigoCorp+"""<br>
                    Atentamente,<br>
                    Equipo Global Red Pymes Personas.<br>
                </body>
            </html>
            """
            sendEmail(subject, txt_content, from_email,to,html_content)

            # Enviar correo a whatsapp
            # Enviar codigo
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:'+numeroTwilio,
                body="""Comuniquese con su asesor del credito, el codigo de autorización es """+codigoUsuario,
                to='whatsapp:'+persona.whatsapp
            )
            message = client.messages.create(
                from_='whatsapp:'+numeroTwilio,
                body="""Comuniquese con su asesor del credito, el codigo de autorización es """+codigoCorp,
                to='whatsapp:+593'+empresa.telefono1
            )

            # Guardar codigo en base
            AutorizacionCredito.objects.create(codigo=codigoCorp,credito=request.data['_id'],entidad=request.data['user_id'])
            AutorizacionCredito.objects.create(codigo=codigoUsuario,credito=request.data['_id'],entidad=request.data['empresaComercial_id'])

            new_serializer_data={'estado': 'ok','codigoUsuario':codigoUsuario,'codigoCorp':codigoCorp}
            #envio de datos
            return Response(new_serializer_data,status=status.HTTP_200_OK)
        except Exception as e: 
            err={"error":'Un error ha ocurrido: {}'.format(e)}  
            createLog(logModel,err,logExcepcion)
            return Response(err, status=status.HTTP_400_BAD_REQUEST) 


