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
    if 'identificacionConyuge' in data:
        identificacionConyuge = data.pop('identificacionConyuge')
        data['identificacionConyuge'] = str(identificacionConyuge).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'papeletaVotacionConyuge' in data:
        papeletaVotacionConyuge = data.pop('papeletaVotacionConyuge')
        data['papeletaVotacionConyuge'] = str(papeletaVotacionConyuge).replace('https://globalredpymes.s3.amazonaws.com/', '')
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
    if 'planillaLuzNegocio' in data:
        planillaLuzNegocio = data.pop('planillaLuzNegocio')
        data['planillaLuzNegocio'] = str(planillaLuzNegocio).replace('https://globalredpymes.s3.amazonaws.com/', '')
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
    if 'facturasVentas2meses' in data:
        facturasVentas2meses = data.pop('facturasVentas2meses')
        data['facturasVentas2meses'] = str(facturasVentas2meses).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'facturasVentas2meses2' in data:
        facturasVentas2meses2 = data.pop('facturasVentas2meses2')
        data['facturasVentas2meses2'] = str(facturasVentas2meses2).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'facturasVentas2meses3' in data:
        facturasVentas2meses3 = data.pop('facturasVentas2meses3')
        data['facturasVentas2meses3'] = str(facturasVentas2meses3).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'facturasVentasCertificado' in data:
        facturasVentasCertificado = data.pop('facturasVentasCertificado')
        data['facturasVentasCertificado'] = str(facturasVentasCertificado).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'facturasCompras2meses' in data:
        facturasCompras2meses = data.pop('facturasCompras2meses')
        data['facturasCompras2meses'] = str(facturasCompras2meses).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'facturasCompras2meses2' in data:
        facturasCompras2meses2 = data.pop('facturasCompras2meses2')
        data['facturasCompras2meses2'] = str(facturasCompras2meses2).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'nombramientoRepresentante' in data:
        nombramientoRepresentante = data.pop('nombramientoRepresentante')
        data['nombramientoRepresentante'] = str(nombramientoRepresentante).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'certificadoSuperintendencia' in data:
        certificadoSuperintendencia = data.pop('certificadoSuperintendencia')
        data['certificadoSuperintendencia'] = str(certificadoSuperintendencia).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'certificadoPatronales' in data:
        certificadoPatronales = data.pop('certificadoPatronales')
        data['certificadoPatronales'] = str(certificadoPatronales).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'nominaSocios' in data:
        nominaSocios = data.pop('nominaSocios')
        data['nominaSocios'] = str(nominaSocios).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'actaJuntaGeneral' in data:
        actaJuntaGeneral = data.pop('actaJuntaGeneral')
        data['actaJuntaGeneral'] = str(actaJuntaGeneral).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'certificadoBancario' in data:
        certificadoBancario = data.pop('certificadoBancario')
        data['certificadoBancario'] = str(certificadoBancario).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'referenciasComerciales' in data:
        referenciasComerciales = data.pop('referenciasComerciales')
        data['referenciasComerciales'] = str(referenciasComerciales).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'balancePerdidasGanancias' in data:
        balancePerdidasGanancias = data.pop('balancePerdidasGanancias')
        data['balancePerdidasGanancias'] = str(balancePerdidasGanancias).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'balanceResultados' in data:
        balanceResultados = data.pop('balanceResultados')
        data['balanceResultados'] = str(balanceResultados).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'declaracionIva' in data:
        declaracionIva = data.pop('declaracionIva')
        data['declaracionIva'] = str(declaracionIva).replace('https://globalredpymes.s3.amazonaws.com/', '')
    if 'estadoCuentaTarjeta' in data:
        estadoCuentaTarjeta = data.pop('estadoCuentaTarjeta')
        data['estadoCuentaTarjeta'] = str(estadoCuentaTarjeta).replace('https://globalredpymes.s3.amazonaws.com/', '')
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
