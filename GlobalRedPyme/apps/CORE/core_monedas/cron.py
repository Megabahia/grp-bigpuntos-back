from .models import Monedas
import boto3
import json
# Importar configuraciones
from apps.config import config
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
            jsonRequest = json.loads(body['Message'])
            print('message', jsonRequest['user_id'])
            # Busca en la bdd las sqs
            monedasUsuario = Monedas.objects.filter(user_id=str(jsonRequest['user_id']), state=1).order_by('-created_at').first()
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
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel, err, logExcepcion)
        return err
