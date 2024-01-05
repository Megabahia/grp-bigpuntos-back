import boto3
import json
# Importar configuraciones
from ...config import config
from .serializers import CreditoPersonasSerializer
from .models import CreditoPersonas
from bson import ObjectId
# logs
from ...CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP
# IMPORTAR ENVIO CONFIGURACION CORREO
from ...config.util2 import sendEmail

# declaracion variables log
datosAux = datosProductosMDP()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


def get_queue_url():
    """
    Este metodo sirve para consumir la cola de aws
    @rtype: No devuelve nada
    """
    print('entro')
    logModel = {
        'endPoint': logApi + 'listOne/',
        'modulo': logModulo,
        'tipo': logExcepcion,
        'accion': 'CRON_SQS_BIGBUNTOS',
        # 'fechaInicio' : str(timezone_now),
        'dataEnviada': '{}',
        # 'fechaFin': str(timezone_now),
        'dataRecibida': '{}'
    }
    try:
        region_name = config.AWS_REGION_NAME
        queue_name = config.AWS_QUEUE_NAME
        max_queue_messages = 10
        aws_access_key_id = config.AWS_ACCESS_KEY_ID_COLAS
        aws_secret_access_key = config.AWS_SECRET_ACCESS_KEY_COLAS
        sqs = boto3.resource('sqs', region_name=region_name,
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)
        queue = sqs.get_queue_by_name(QueueName=queue_name)

        # Consultar la cola maximo 10 mensajes
        for message in queue.receive_messages(MaxNumberOfMessages=max_queue_messages):
            # process message body
            body = json.loads(message.body)
            print('llego las colas')
            if body['Subject'] != 'IFIS':
                jsonRequest = json.loads(body['Message'])
                _idCredidPerson = json.loads(body['Message'])['external_id']
                jsonRequest.pop('_id')
                # Busca en la bdd las sqs
                query = CreditoPersonas.objects.filter(pk=ObjectId(_idCredidPerson), state=1).first()
                if query is None:
                    if type(jsonRequest['empresaInfo']) == str and jsonRequest['empresaInfo'] != '':
                        jsonRequest['empresaInfo'] = json.loads(jsonRequest['empresaInfo'])
                    if 'tipoCredito' in jsonRequest and jsonRequest['tipoCredito'] == '':
                        jsonRequest['tipoCredito'] = jsonRequest['canal']
                    if 'solicitudCredito' in jsonRequest:
                        jsonRequest.pop('solicitudCredito')
                    if 'buroCreditoIfis' in jsonRequest:
                        jsonRequest.pop('buroCreditoIfis')
                    if 'pagare' in jsonRequest:
                        jsonRequest.pop('pagare')
                    if 'contratosCuenta' in jsonRequest:
                        jsonRequest.pop('contratosCuenta')
                    if 'tablaAmortizacion' in jsonRequest:
                        jsonRequest.pop('tablaAmortizacion')
                    # Guardamos
                    credito = CreditoPersonas.objects.create(**jsonRequest)
                else:
                    CreditoPersonas.objects.filter(pk=ObjectId(_idCredidPerson)).update(**jsonRequest)
                    print('se actualiza')
                    credito = query
                # Crear objeto en firebase para las notificaciones
                config.FIREBASE_DB.collection('creditosPersonas').document(str(credito._id)).set(jsonRequest)
                if jsonRequest['email'] == 'Aprobado':
                    usuario = jsonRequest['user']
                    email = usuario['email'] if usuario else jsonRequest['email']
                    if email == '' or email is None:
                        email = jsonRequest['empresaInfo']['correo']
                    # Enviar correo de aprobado
                    enviarCorreoSolicitud(email)
            # Borramos SQS
            message.delete()
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return err


def enviarCorreoSolicitud(email):
    subject, from_email, to = 'Generación de código para crédito aprobado', "credicompra.bigpuntos@corporacionomniglobal.com", \
                              email
    txt_content = f"""
                        Global RedPyme - Crédito Pagos ha recibido su solicitud, estaremos en contacto con usted a la brevedad posible.
                            Crédito Pagos es la mejor opción para el crecimiento de su negocio
                        Atentamente,
                        Global RedPyme – Crédito Pagos
    """
    html_content = f"""
                <html>
                    <body>
                        <h1>FELICIDADES!!</h1>
                        <p>Su microcrédito línea de crédito para pago a proveedores ha sido <b>APROBADO.</b></p>
                        <br>
                        <br>
                        <p>Realice los siguientes pasos:</p>
                        <ul>
                        <li>
                        Ingrese a: {config.API_FRONT_END_IFISCLIENTES}/personas/registroFirmaElectronica y
                        cargue su firma electrónica en nuestra plataforma. Recuerde que al hacerlo, autoriza a la Plataforma y 
                        Entidad Financiera a realizar movimientos desde su cuenta con el único fin de completar el 
                        proceso del PAGO A SUS PROVEEDORES desde su cuenta.
                        </li>
                        <li>
                        Registre a sus proveedores a través de
                         {config.API_FRONT_END_IFISCLIENTES}/personas/registroProveedores para realizar
                          el pago de forma fácil y rápida.
                        </li>
                        </ul>
                        <br>
                        <br>
                        <h3><b>Crédito Pagos es la mejor opción para el crecimiento de su negocio</b></h3>
                        <br>
                        Atentamente,
                        <br>
                        Global RedPyme – Crédito Pagos
                        <br>
                    </body>
                </html>
                """
    sendEmail(subject, txt_content, from_email, to, html_content)