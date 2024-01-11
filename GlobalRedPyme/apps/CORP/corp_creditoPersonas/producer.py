import boto3
import json
# Importar configuraciones
from apps.config import config
from urllib.parse import unquote
import environ

from .s3 import replicate


def publish(data):
    """
    Este metodo sirve para publiar en la cola de aws
    @type data: REcibe los datos que se van a publicar
    @rtype: No devuelve nada
    """
    topicArn = config.AWS_TOPIC_ARN
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )
    env = environ.Env()
    environ.Env.read_env()  # LEE ARCHIVO .ENV
    campos = [
        'pagare', 'contratosCuenta', 'tablaAmortizacion',
        'reporteBuro', 'identificacion', 'identificacionConyuge',
        'papeletaVotacionConyuge', 'ruc', 'rolesPago', 'panillaIESS',
        'documentoAprobacion', 'papeletaVotacion', 'planillaLuzDomicilio',
        'planillaLuzNegocio', 'matriculaVehiculo', 'impuestoPredial',
        'buroCredito', 'mecanizadoIess', 'fotoCarnet',
        'facturasVentas2meses', 'facturasVentas2meses2', 'facturasVentas2meses3',
        'facturasVentasCertificado', 'facturasCompras2meses',
        'facturasCompras2meses2', 'nombramientoRepresentante',
        'certificadoSuperintendencia', 'certificadoPatronales', 'nominaSocios',
        'actaJuntaGeneral', 'certificadoBancario', 'referenciasComerciales',
        'balancePerdidasGanancias', 'balanceResultados', 'declaracionIva',
        'estadoCuentaTarjeta', 'facturasPendiente', 'imagen', 'imagenComercial',
        'autorizacion', 'cedulaGarante', 'papeletaVotacionGarante', 'fotoGarante',
        'impuestoPredialGarante', 'matriculaVehiculoGarante',
        'planillaDomicilioGarante', 'solicitudCredito', 'buroCreditoIfis',
    ]

    for campo in campos:
        if campo in data:
            valor = data.pop(campo)
            valor = unquote(str(valor).replace(env.str('URL_BUCKET'), ''))
            print(campo, valor)
            if valor != 'None':
                data[campo] = valor
                replicate(valor)

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
