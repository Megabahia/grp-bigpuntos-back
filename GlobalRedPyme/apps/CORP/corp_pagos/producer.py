import boto3
import json
# Importar configuraciones
from apps.config import config


def publish(data):
    """
    Este metodo sirve para enviar a la cola de aws de los pagos
    @type data: El campo data recibe el registro de pago
    @rtype: Noo devuelve nada
    """
    topicArn = config.AWS_TOPIC_ARN_PAGOS
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
