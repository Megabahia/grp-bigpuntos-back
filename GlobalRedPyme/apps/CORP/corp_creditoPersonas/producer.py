import boto3
import json
# Importar configuraciones
from apps.config import config
from urllib.parse import unquote
import environ


def publish(data):
    topicArn = config.AWS_TOPIC_ARN
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=config.AWS_ACCESS_KEY_ID_COLAS,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY_COLAS,
        region_name=config.AWS_REGION_NAME,
    )
    env = environ.Env()
    environ.Env.read_env()  # LEE ARCHIVO .ENV
    if 'reporteBuro' in data:
        reporteBuro = data.pop('reporteBuro')
        data['reporteBuro'] = unquote(str(reporteBuro).replace(env.str('URL_BUCKET'), ''))
        if data['reporteBuro'] == 'None':
            data.pop('reporteBuro')
    if 'identificacion' in data:
        identificacion = data.pop('identificacion')
        data['identificacion'] = unquote(str(identificacion).replace(env.str('URL_BUCKET'), ''))
        if data['identificacion'] == 'None':
            data.pop('identificacion')
    if 'identificacionConyuge' in data:
        identificacionConyuge = data.pop('identificacionConyuge')
        data['identificacionConyuge'] = unquote(str(identificacionConyuge).replace(env.str('URL_BUCKET'), ''))
        if data['identificacionConyuge'] == 'None':
            data.pop('identificacionConyuge')
    if 'papeletaVotacionConyuge' in data:
        papeletaVotacionConyuge = data.pop('papeletaVotacionConyuge')
        data['papeletaVotacionConyuge'] = unquote(str(papeletaVotacionConyuge).replace(env.str('URL_BUCKET'), ''))
        if data['papeletaVotacionConyuge'] == 'None':
            data.pop('papeletaVotacionConyuge')
    if 'ruc' in data:
        ruc = data.pop('ruc')
        data['ruc'] = unquote(str(ruc).replace(env.str('URL_BUCKET'), ''))
        if data['ruc'] == 'None':
            data.pop('ruc')
    if 'rolesPago' in data:
        rolesPago = data.pop('rolesPago')
        data['rolesPago'] = unquote(str(rolesPago).replace(env.str('URL_BUCKET'), ''))
        if data['rolesPago'] == 'None':
            data.pop('rolesPago')
    if 'panillaIESS' in data:
        panillaIESS = data.pop('panillaIESS')
        data['panillaIESS'] = unquote(str(panillaIESS).replace(env.str('URL_BUCKET'), ''))
        if data['panillaIESS'] == 'None':
            data.pop('panillaIESS')
    if 'documentoAprobacion' in data:
        documentoAprobacion = data.pop('documentoAprobacion')
        data['documentoAprobacion'] = unquote(str(documentoAprobacion).replace(env.str('URL_BUCKET'), ''))
        if data['documentoAprobacion'] == 'None':
            data.pop('documentoAprobacion')
    if 'papeletaVotacion' in data:
        papeletaVotacion = data.pop('papeletaVotacion')
        data['papeletaVotacion'] = unquote(str(papeletaVotacion).replace(env.str('URL_BUCKET'), ''))
        if data['papeletaVotacion'] == 'None':
            data.pop('papeletaVotacion')
    if 'planillaLuzDomicilio' in data:
        planillaLuzDomicilio = data.pop('planillaLuzDomicilio')
        data['planillaLuzDomicilio'] = unquote(str(planillaLuzDomicilio).replace(env.str('URL_BUCKET'), ''))
        if data['planillaLuzDomicilio'] == 'None':
            data.pop('planillaLuzDomicilio')
    if 'planillaLuzNegocio' in data:
        planillaLuzNegocio = data.pop('planillaLuzNegocio')
        data['planillaLuzNegocio'] = unquote(str(planillaLuzNegocio).replace(env.str('URL_BUCKET'), ''))
        if data['planillaLuzNegocio'] == 'None':
            data.pop('planillaLuzNegocio')
    if 'matriculaVehiculo' in data:
        matriculaVehiculo = data.pop('matriculaVehiculo')
        data['matriculaVehiculo'] = unquote(str(matriculaVehiculo).replace(env.str('URL_BUCKET'), ''))
        if data['matriculaVehiculo'] == 'None':
            data.pop('matriculaVehiculo')
    if 'impuestoPredial' in data:
        impuestoPredial = data.pop('impuestoPredial')
        data['impuestoPredial'] = unquote(str(impuestoPredial).replace(env.str('URL_BUCKET'), ''))
        if data['impuestoPredial'] == 'None':
            data.pop('impuestoPredial')
    if 'buroCredito' in data:
        buroCredito = data.pop('buroCredito')
        data['buroCredito'] = unquote(str(buroCredito).replace(env.str('URL_BUCKET'), ''))
        if data['buroCredito'] == 'None':
            data.pop('buroCredito')
    if 'mecanizadoIess' in data:
        mecanizadoIess = data.pop('mecanizadoIess')
        data['mecanizadoIess'] = unquote(str(mecanizadoIess).replace(env.str('URL_BUCKET'), ''))
        if data['mecanizadoIess'] == 'None':
            data.pop('mecanizadoIess')
    if 'fotoCarnet' in data:
        fotoCarnet = data.pop('fotoCarnet')
        data['fotoCarnet'] = unquote(str(fotoCarnet).replace(env.str('URL_BUCKET'), ''))
        if data['fotoCarnet'] == 'None':
            data.pop('fotoCarnet')
    if 'facturasVentas2meses' in data:
        facturasVentas2meses = data.pop('facturasVentas2meses')
        data['facturasVentas2meses'] = unquote(str(facturasVentas2meses).replace(env.str('URL_BUCKET'), ''))
        if data['facturasVentas2meses'] == 'None':
            data.pop('facturasVentas2meses')
    if 'facturasVentas2meses2' in data:
        facturasVentas2meses2 = data.pop('facturasVentas2meses2')
        data['facturasVentas2meses2'] = unquote(str(facturasVentas2meses2).replace(env.str('URL_BUCKET'), ''))
        if data['facturasVentas2meses2'] == 'None':
            data.pop('facturasVentas2meses2')
    if 'facturasVentas2meses3' in data:
        facturasVentas2meses3 = data.pop('facturasVentas2meses3')
        data['facturasVentas2meses3'] = unquote(str(facturasVentas2meses3).replace(env.str('URL_BUCKET'), ''))
        if data['facturasVentas2meses3'] == 'None':
            data.pop('facturasVentas2meses3')
    if 'facturasVentasCertificado' in data:
        facturasVentasCertificado = data.pop('facturasVentasCertificado')
        data['facturasVentasCertificado'] = unquote(str(facturasVentasCertificado).replace(env.str('URL_BUCKET'), ''))
        if data['facturasVentasCertificado'] == 'None':
            data.pop('facturasVentasCertificado')
    if 'facturasCompras2meses' in data:
        facturasCompras2meses = data.pop('facturasCompras2meses')
        data['facturasCompras2meses'] = unquote(str(facturasCompras2meses).replace(env.str('URL_BUCKET'), ''))
        if data['facturasCompras2meses'] == 'None':
            data.pop('facturasCompras2meses')
    if 'facturasCompras2meses2' in data:
        facturasCompras2meses2 = data.pop('facturasCompras2meses2')
        data['facturasCompras2meses2'] = unquote(str(facturasCompras2meses2).replace(env.str('URL_BUCKET'), ''))
        if data['facturasCompras2meses2'] == 'None':
            data.pop('facturasCompras2meses2')
    if 'nombramientoRepresentante' in data:
        nombramientoRepresentante = data.pop('nombramientoRepresentante')
        data['nombramientoRepresentante'] = unquote(str(nombramientoRepresentante).replace(env.str('URL_BUCKET'), ''))
        if data['nombramientoRepresentante'] == 'None':
            data.pop('nombramientoRepresentante')
    if 'certificadoSuperintendencia' in data:
        certificadoSuperintendencia = data.pop('certificadoSuperintendencia')
        data['certificadoSuperintendencia'] = unquote(str(certificadoSuperintendencia).replace(env.str('URL_BUCKET'), ''))
        if data['certificadoSuperintendencia'] == 'None':
            data.pop('certificadoSuperintendencia')
    if 'certificadoPatronales' in data:
        certificadoPatronales = data.pop('certificadoPatronales')
        data['certificadoPatronales'] = unquote(str(certificadoPatronales).replace(env.str('URL_BUCKET'), ''))
        if data['certificadoPatronales'] == 'None':
            data.pop('certificadoPatronales')
    if 'nominaSocios' in data:
        nominaSocios = data.pop('nominaSocios')
        data['nominaSocios'] = unquote(str(nominaSocios).replace(env.str('URL_BUCKET'), ''))
        if data['nominaSocios'] == 'None':
            data.pop('nominaSocios')
    if 'actaJuntaGeneral' in data:
        actaJuntaGeneral = data.pop('actaJuntaGeneral')
        data['actaJuntaGeneral'] = unquote(str(actaJuntaGeneral).replace(env.str('URL_BUCKET'), ''))
        if data['actaJuntaGeneral'] == 'None':
            data.pop('actaJuntaGeneral')
    if 'certificadoBancario' in data:
        certificadoBancario = data.pop('certificadoBancario')
        data['certificadoBancario'] = unquote(str(certificadoBancario).replace(env.str('URL_BUCKET'), ''))
        if data['certificadoBancario'] == 'None':
            data.pop('certificadoBancario')
    if 'referenciasComerciales' in data:
        referenciasComerciales = data.pop('referenciasComerciales')
        data['referenciasComerciales'] = unquote(str(referenciasComerciales).replace(env.str('URL_BUCKET'), ''))
        if data['referenciasComerciales'] == 'None':
            data.pop('referenciasComerciales')
    if 'balancePerdidasGanancias' in data:
        balancePerdidasGanancias = data.pop('balancePerdidasGanancias')
        data['balancePerdidasGanancias'] = unquote(str(balancePerdidasGanancias).replace(env.str('URL_BUCKET'), ''))
        if data['balancePerdidasGanancias'] == 'None':
            data.pop('balancePerdidasGanancias')
    if 'balanceResultados' in data:
        balanceResultados = data.pop('balanceResultados')
        data['balanceResultados'] = unquote(str(balanceResultados).replace(env.str('URL_BUCKET'), ''))
        if data['balanceResultados'] == 'None':
            data.pop('balanceResultados')
    if 'declaracionIva' in data:
        declaracionIva = data.pop('declaracionIva')
        data['declaracionIva'] = unquote(str(declaracionIva).replace(env.str('URL_BUCKET'), ''))
        if data['declaracionIva'] == 'None':
            data.pop('declaracionIva')
    if 'estadoCuentaTarjeta' in data:
        estadoCuentaTarjeta = data.pop('estadoCuentaTarjeta')
        data['estadoCuentaTarjeta'] = unquote(str(estadoCuentaTarjeta).replace(env.str('URL_BUCKET'), ''))
        if data['estadoCuentaTarjeta'] == 'None':
            data.pop('estadoCuentaTarjeta')
    if 'facturasPendiente' in data:
        facturasPendiente = data.pop('facturasPendiente')
        data['facturasPendiente'] = unquote(str(facturasPendiente).replace(env.str('URL_BUCKET'), ''))
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
    if 'autorizacion' in data:
        autorizacion = data.pop('autorizacion')
        data['autorizacion'] = unquote(str(autorizacion).replace(env.str('URL_BUCKET'), ''))
        if data['autorizacion'] == 'None':
            data.pop('autorizacion')
    if 'cedulaGarante' in data:
        cedulaGarante = data.pop('cedulaGarante')
        data['cedulaGarante'] = unquote(str(cedulaGarante).replace(env.str('URL_BUCKET'), ''))
        if data['cedulaGarante'] == 'None':
            data.pop('cedulaGarante')
    if 'papeletaVotacionGarante' in data:
        papeletaVotacionGarante = data.pop('papeletaVotacionGarante')
        data['papeletaVotacionGarante'] = unquote(str(papeletaVotacionGarante).replace(env.str('URL_BUCKET'), ''))
        if data['papeletaVotacionGarante'] == 'None':
            data.pop('papeletaVotacionGarante')
    if 'fotoGarante' in data:
        fotoGarante = data.pop('fotoGarante')
        data['fotoGarante'] = unquote(str(fotoGarante).replace(env.str('URL_BUCKET'), ''))
        if data['fotoGarante'] == 'None':
            data.pop('fotoGarante')
    if 'impuestoPredialGarante' in data:
        impuestoPredialGarante = data.pop('impuestoPredialGarante')
        data['impuestoPredialGarante'] = unquote(str(impuestoPredialGarante).replace(env.str('URL_BUCKET'), ''))
        if data['impuestoPredialGarante'] == 'None':
            data.pop('impuestoPredialGarante')
    if 'matriculaVehiculoGarante' in data:
        matriculaVehiculoGarante = data.pop('matriculaVehiculoGarante')
        data['matriculaVehiculoGarante'] = unquote(str(matriculaVehiculoGarante).replace(env.str('URL_BUCKET'), ''))
        if data['matriculaVehiculoGarante'] == 'None':
            data.pop('matriculaVehiculoGarante')
    if 'planillaDomicilioGarante' in data:
        planillaDomicilioGarante = data.pop('planillaDomicilioGarante')
        data['planillaDomicilioGarante'] = unquote(str(planillaDomicilioGarante).replace(env.str('URL_BUCKET'), ''))
        if data['planillaDomicilioGarante'] == 'None':
            data.pop('planillaDomicilioGarante')

    response = snsClient.publish(
        TopicArn=topicArn,
        Message=json.dumps(data),
        Subject='PURCHASE',
        MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "PURCHASE"}}
    )
    print(response['ResponseMetadata']['HTTPStatusCode'])
