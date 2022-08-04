import boto3
import json
# Timezone
from django.utils import timezone
# Importar configuraciones
from apps.config import config
from apps.CORP.corp_creditoPersonas.models import CodigoCreditoPreaprobado
from bson import ObjectId
#logs
from apps.CENTRAL.central_logs.methods import createLog,datosTipoLog, datosSQS
#declaracion variables log
datosAux=datosSQS()
datosTipoLogAux=datosTipoLog()
#asignacion datos modulo
logModulo=datosAux['modulo']
logApi=datosAux['api']
#asignacion tipo de datos
logTransaccion=datosTipoLogAux['transaccion']
logExcepcion=datosTipoLogAux['excepcion']

def codigoCreditoPreaprobado():
    timezone_now = timezone.localtime(timezone.now())
    logModel = {
        'endPoint': logApi+'guardar/',
        'modulo':logModulo,
        'tipo' : logExcepcion,
        'accion' : 'CRON_SQS_BIGBUNTOS',
        'fechaInicio' : str(timezone_now),
        'dataEnviada' : '{}',
        'fechaFin': str(timezone_now),
        'dataRecibida' : '{}'
    }
    try:
        region_name = config.AWS_REGION_NAME
        queue_name = config.AWS_QUEUE_NAME_CODIGOS
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
            # Busca en la bdd las sqs
            query = CodigoCreditoPreaprobado.objects.create(**jsonRequest)
            if query is not None:
                # Borramos SQS
                message.delete()
    except Exception as e:
        err={"error":'Un error ha ocurrido: {}'.format(e)}
        createLog(logModel,err,logExcepcion)
        return err