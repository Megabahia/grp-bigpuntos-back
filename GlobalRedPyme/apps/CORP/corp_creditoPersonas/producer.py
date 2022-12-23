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

    if 'reporteBuro' in data:
        reporteBuro = data.pop('reporteBuro')
        data['reporteBuro'] = str(reporteBuro).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'identificacion' in data:
        identificacion = data.pop('identificacion')
        data['identificacion'] = str(identificacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'ruc' in data:
        ruc = data.pop('ruc')
        data['ruc'] = str(ruc).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'rolesPago' in data:
        rolesPago = data.pop('rolesPago')
        data['rolesPago'] = str(rolesPago).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'panillaIESS' in data:
        panillaIESS = data.pop('panillaIESS')
        data['panillaIESS'] = str(panillaIESS).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'documentoAprobacion' in data:
        documentoAprobacion = data.pop('documentoAprobacion')
        data['documentoAprobacion'] = str(documentoAprobacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'papeletaVotacion' in data:
        papeletaVotacion = data.pop('papeletaVotacion')
        data['papeletaVotacion'] = str(papeletaVotacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'planillaLuzDomicilio' in data:
        planillaLuzDomicilio = data.pop('planillaLuzDomicilio')
        data['planillaLuzDomicilio'] = str(planillaLuzDomicilio).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'matriculaVehiculo' in data:
        matriculaVehiculo = data.pop('matriculaVehiculo')
        data['matriculaVehiculo'] = str(matriculaVehiculo).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'impuestoPredial' in data:
        impuestoPredial = data.pop('impuestoPredial')
        data['impuestoPredial'] = str(impuestoPredial).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'buroCredito' in data:
        buroCredito = data.pop('buroCredito')
        data['buroCredito'] = str(buroCredito).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'mecanizadoIess' in data:
        mecanizadoIess = data.pop('mecanizadoIess')
        data['mecanizadoIess'] = str(mecanizadoIess).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'fotoCarnet' in data:
        fotoCarnet = data.pop('fotoCarnet')
        data['fotoCarnet'] = str(fotoCarnet).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'imagen' in data:
        data.pop('imagen')
    if 'imagenComercial' in data:
        data.pop('imagenComercial')

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
