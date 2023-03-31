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
        if data['reporteBuro'] == 'None':
            data.pop('reporteBuro')
    if 'identificacion' in data:
        identificacion = data.pop('identificacion')
        data['identificacion'] = str(identificacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['identificacion'] == 'None':
            data.pop('identificacion')
    if 'identificacionConyuge' in data:
        identificacionConyuge = data.pop('identificacionConyuge')
        data['identificacionConyuge'] = str(identificacionConyuge).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['identificacionConyuge'] == 'None':
            data.pop('identificacionConyuge')
    if 'papeletaVotacionConyuge' in data:
        papeletaVotacionConyuge = data.pop('papeletaVotacionConyuge')
        data['papeletaVotacionConyuge'] = str(papeletaVotacionConyuge).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['papeletaVotacionConyuge'] == 'None':
            data.pop('papeletaVotacionConyuge')
    if 'ruc' in data:
        ruc = data.pop('ruc')
        data['ruc'] = str(ruc).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['ruc'] == 'None':
            data.pop('ruc')
    if 'rolesPago' in data:
        rolesPago = data.pop('rolesPago')
        data['rolesPago'] = str(rolesPago).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['rolesPago'] == 'None':
            data.pop('rolesPago')
    if 'panillaIESS' in data:
        panillaIESS = data.pop('panillaIESS')
        data['panillaIESS'] = str(panillaIESS).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['panillaIESS'] == 'None':
            data.pop('panillaIESS')
    if 'documentoAprobacion' in data:
        documentoAprobacion = data.pop('documentoAprobacion')
        data['documentoAprobacion'] = str(documentoAprobacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['documentoAprobacion'] == 'None':
            data.pop('documentoAprobacion')
    if 'papeletaVotacion' in data:
        papeletaVotacion = data.pop('papeletaVotacion')
        data['papeletaVotacion'] = str(papeletaVotacion).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['papeletaVotacion'] == 'None':
            data.pop('papeletaVotacion')
    if 'planillaLuzDomicilio' in data:
        planillaLuzDomicilio = data.pop('planillaLuzDomicilio')
        data['planillaLuzDomicilio'] = str(planillaLuzDomicilio).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['planillaLuzDomicilio'] == 'None':
            data.pop('planillaLuzDomicilio')
    if 'planillaLuzNegocio' in data:
        planillaLuzNegocio = data.pop('planillaLuzNegocio')
        data['planillaLuzNegocio'] = str(planillaLuzNegocio).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['planillaLuzNegocio'] == 'None':
            data.pop('planillaLuzNegocio')
    if 'matriculaVehiculo' in data:
        matriculaVehiculo = data.pop('matriculaVehiculo')
        data['matriculaVehiculo'] = str(matriculaVehiculo).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['matriculaVehiculo'] == 'None':
            data.pop('matriculaVehiculo')
    if 'impuestoPredial' in data:
        impuestoPredial = data.pop('impuestoPredial')
        data['impuestoPredial'] = str(impuestoPredial).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['impuestoPredial'] == 'None':
            data.pop('impuestoPredial')
    if 'buroCredito' in data:
        buroCredito = data.pop('buroCredito')
        data['buroCredito'] = str(buroCredito).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['buroCredito'] == 'None':
            data.pop('buroCredito')
    if 'mecanizadoIess' in data:
        mecanizadoIess = data.pop('mecanizadoIess')
        data['mecanizadoIess'] = str(mecanizadoIess).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['mecanizadoIess'] == 'None':
            data.pop('mecanizadoIess')
    if 'fotoCarnet' in data:
        fotoCarnet = data.pop('fotoCarnet')
        data['fotoCarnet'] = str(fotoCarnet).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['fotoCarnet'] == 'None':
            data.pop('fotoCarnet')
    if 'facturasVentas2meses' in data:
        facturasVentas2meses = data.pop('facturasVentas2meses')
        data['facturasVentas2meses'] = str(facturasVentas2meses).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasVentas2meses'] == 'None':
            data.pop('facturasVentas2meses')
    if 'facturasVentas2meses2' in data:
        facturasVentas2meses2 = data.pop('facturasVentas2meses2')
        data['facturasVentas2meses2'] = str(facturasVentas2meses2).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasVentas2meses2'] == 'None':
            data.pop('facturasVentas2meses2')
    if 'facturasVentas2meses3' in data:
        facturasVentas2meses3 = data.pop('facturasVentas2meses3')
        data['facturasVentas2meses3'] = str(facturasVentas2meses3).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasVentas2meses3'] == 'None':
            data.pop('facturasVentas2meses3')
    if 'facturasVentasCertificado' in data:
        facturasVentasCertificado = data.pop('facturasVentasCertificado')
        data['facturasVentasCertificado'] = str(facturasVentasCertificado).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasVentasCertificado'] == 'None':
            data.pop('facturasVentasCertificado')
    if 'facturasCompras2meses' in data:
        facturasCompras2meses = data.pop('facturasCompras2meses')
        data['facturasCompras2meses'] = str(facturasCompras2meses).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasCompras2meses'] == 'None':
            data.pop('facturasCompras2meses')
    if 'facturasCompras2meses2' in data:
        facturasCompras2meses2 = data.pop('facturasCompras2meses2')
        data['facturasCompras2meses2'] = str(facturasCompras2meses2).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasCompras2meses2'] == 'None':
            data.pop('facturasCompras2meses2')
    if 'nombramientoRepresentante' in data:
        nombramientoRepresentante = data.pop('nombramientoRepresentante')
        data['nombramientoRepresentante'] = str(nombramientoRepresentante).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['nombramientoRepresentante'] == 'None':
            data.pop('nombramientoRepresentante')
    if 'certificadoSuperintendencia' in data:
        certificadoSuperintendencia = data.pop('certificadoSuperintendencia')
        data['certificadoSuperintendencia'] = str(certificadoSuperintendencia).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['certificadoSuperintendencia'] == 'None':
            data.pop('certificadoSuperintendencia')
    if 'certificadoPatronales' in data:
        certificadoPatronales = data.pop('certificadoPatronales')
        data['certificadoPatronales'] = str(certificadoPatronales).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['certificadoPatronales'] == 'None':
            data.pop('certificadoPatronales')
    if 'nominaSocios' in data:
        nominaSocios = data.pop('nominaSocios')
        data['nominaSocios'] = str(nominaSocios).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['nominaSocios'] == 'None':
            data.pop('nominaSocios')
    if 'actaJuntaGeneral' in data:
        actaJuntaGeneral = data.pop('actaJuntaGeneral')
        data['actaJuntaGeneral'] = str(actaJuntaGeneral).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['actaJuntaGeneral'] == 'None':
            data.pop('actaJuntaGeneral')
    if 'certificadoBancario' in data:
        certificadoBancario = data.pop('certificadoBancario')
        data['certificadoBancario'] = str(certificadoBancario).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['certificadoBancario'] == 'None':
            data.pop('certificadoBancario')
    if 'referenciasComerciales' in data:
        referenciasComerciales = data.pop('referenciasComerciales')
        data['referenciasComerciales'] = str(referenciasComerciales).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['referenciasComerciales'] == 'None':
            data.pop('referenciasComerciales')
    if 'balancePerdidasGanancias' in data:
        balancePerdidasGanancias = data.pop('balancePerdidasGanancias')
        data['balancePerdidasGanancias'] = str(balancePerdidasGanancias).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['balancePerdidasGanancias'] == 'None':
            data.pop('balancePerdidasGanancias')
    if 'balanceResultados' in data:
        balanceResultados = data.pop('balanceResultados')
        data['balanceResultados'] = str(balanceResultados).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['balanceResultados'] == 'None':
            data.pop('balanceResultados')
    if 'declaracionIva' in data:
        declaracionIva = data.pop('declaracionIva')
        data['declaracionIva'] = str(declaracionIva).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['declaracionIva'] == 'None':
            data.pop('declaracionIva')
    if 'estadoCuentaTarjeta' in data:
        estadoCuentaTarjeta = data.pop('estadoCuentaTarjeta')
        data['estadoCuentaTarjeta'] = str(estadoCuentaTarjeta).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['estadoCuentaTarjeta'] == 'None':
            data.pop('estadoCuentaTarjeta')
    if 'facturasPendiente' in data:
        facturasPendiente = data.pop('facturasPendiente')
        data['facturasPendiente'] = str(facturasPendiente).replace('https://globalredpymes.s3.amazonaws.com/', '')
        if data['facturasPendiente'] == 'None':
            data.pop('facturasPendiente')
    if 'imagen' in data:
        data.pop('imagen')
        if data['imagen'] == 'None':
            data.pop('imagen')
    if 'imagenComercial' in data:
        data.pop('imagenComercial')
        if data['imagenComercial'] == 'None':
            data.pop('imagenComercial')

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
