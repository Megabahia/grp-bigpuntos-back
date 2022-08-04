import boto3
import json
# Importar configuraciones
from apps.config import config


def publish(data):
    topicArn = config.AWS_TOPIC_ARN
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )

    reporteBuro = data.pop('reporteBuro')
    data['reporteBuro'] = str(reporteBuro).replace('https://globalredpymes.s3.amazonaws.com/','')
    identificacion = data.pop('identificacion')
    data['identificacion'] = str(identificacion).replace('https://globalredpymes.s3.amazonaws.com/','')
    ruc = data.pop('ruc')
    data['ruc'] = str(ruc).replace('https://globalredpymes.s3.amazonaws.com/','')
    rolesPago = data.pop('rolesPago')
    data['rolesPago'] = str(rolesPago).replace('https://globalredpymes.s3.amazonaws.com/','')
    panillaIESS = data.pop('panillaIESS')
    data['panillaIESS'] = str(panillaIESS).replace('https://globalredpymes.s3.amazonaws.com/','')
    documentoAprobacion = data.pop('documentoAprobacion')
    data['documentoAprobacion'] = str(documentoAprobacion).replace('https://globalredpymes.s3.amazonaws.com/','')
    data.pop('imagen')
    data.pop('imagenComercial')

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType":{"DataType":"String","StringValue":"PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])

    
