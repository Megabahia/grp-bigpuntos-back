from apps.CORP.corp_pagos.models import  Pagos
from apps.CORE.core_monedas.models import Monedas
from django.utils import timezone

def hi():
    timezone_now = timezone.localtime(timezone.now())
    pagos = Pagos.objects.filter(duracion__lte=timezone_now,state=1)

    f = open('/home/sysadmin/prueba.txt','a')
    for pago in pagos:
        # monedasUsuario = Monedas.objects.filter(user_id=pago.user_id,state=1).order_by('-created_at').first()
        # data = {
        #     'user_id': pago.user_id,
        #     'tipo': 'Credito',
        #     'estado': 'aprobado',
        #     'credito': pago.monto,
        #     'saldo': monedasUsuario.saldo + pago.monto,
        #     'descripcion': 'Devolución de monedas al no usar el comprobante de pago.'
        # }
        # Monedas.objects.create(**data)
        f.write(pago)
        f.write("\n ********* \n")
    f.close()


    