from .models import Monedas
import boto3
import json
# Importar configuraciones
from apps.config import config
from bson import ObjectId
# logs
from ...CENTRAL.central_logs.methods import createLog, datosTipoLog, datosProductosMDP

from ...CORP.corp_empresas.models import Empresas
from ...PERSONAS.personas_personas.models import Personas
from ...PERSONAS.personas_personas.security import encriptar

# declaracion variables log
datosAux = datosProductosMDP()
datosTipoLogAux = datosTipoLog()
# asignacion datos modulo
logModulo = datosAux['modulo']
logApi = datosAux['api']
# asignacion tipo de datos
logTransaccion = datosTipoLogAux['transaccion']
logExcepcion = datosTipoLogAux['excepcion']


# ESte metodo realiza la tarea de consultar las monedas de la cola de aws para registrar el movimiento de las monedas
def hi():
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
        queue_name = config.AWS_QUEUE_NAME_MONEDAS
        print(queue_name)
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
            if body['Subject'] != 'Credito':
                jsonRequest = json.loads(body['Message'])
                print('message', jsonRequest['user_id'])
                # Busca en la bdd las sqs
                monedasUsuario = Monedas.objects.filter(user_id=str(jsonRequest['user_id']), state=1).order_by(
                    '-created_at').first()
                data = {
                    'user_id': jsonRequest['user_id'],
                    'empresa_id': jsonRequest['empresa_id'],
                    'tipo': 'Debito',
                    'estado': 'aprobado',
                    'debito': jsonRequest['debito'],
                    'saldo': monedasUsuario.saldo - float(jsonRequest['debito']),
                    'descripcion': 'Compra de productos.'
                }
                Monedas.objects.create(**data)
                # Borramos SQS
                message.delete()
                print('se borro')
            else:
                jsonRequest = json.loads(body['Message'])
                # Busca en la bdd las sqs
                monedasUsuario = Monedas.objects.filter(identificacion=str(jsonRequest[1]), email=str(jsonRequest[5]),
                                                        state=1).order_by(
                    '-created_at').first()
                hash_identificacion = encriptar(jsonRequest[1])
                hash_email = encriptar(jsonRequest[5])
                persona = Personas.objects.filter(identificacion=hash_identificacion, email=hash_email, state=1).first()
                empresa = Empresas.objects.filter(ruc=jsonRequest[6]).first()
                data = {
                    'user_id': persona.user_id if persona is not None else None,
                    'identificacion': jsonRequest[1],
                    'nombres': jsonRequest[2],
                    'apellidos': jsonRequest[3],
                    'email': jsonRequest[5],
                    'empresa_id': empresa._id if empresa is not None else None,
                    'tipo': 'Credito',
                    'estado': 'aprobado',
                    'credito': jsonRequest[4],
                    'saldo': monedasUsuario.saldo + float(jsonRequest[4]) if monedasUsuario else float(jsonRequest[4]),
                    'descripcion': jsonRequest[8]
                }
                Monedas.objects.create(**data)
                # Borramos SQS
                message.delete()
                print('se borro')
    except Exception as e:
        print('error', e)
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return err
