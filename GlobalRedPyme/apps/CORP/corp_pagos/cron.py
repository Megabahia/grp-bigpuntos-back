from apps.CORP.corp_pagos.models import  Pagos
from apps.CORE.core_monedas.models import Monedas
from django.utils import timezone

def hi():
    # f = open('/home/sysadmin/prueba.txt','a')
    timezone_now = timezone.localtime(timezone.now())
    pagos = Pagos.objects.filter(duracion__lte=str(timezone_now),state=1)

    for pago in pagos:
        monedasUsuario = Monedas.objects.filter(user_id=pago.user_id,state=1).order_by('-created_at').first()
        data = {
            'user_id': pago.user_id,
            'empresa_id': pago.empresa_id,
            'tipo': 'Credito',
            'estado': 'aprobado',
            'credito': pago.monto,
            'saldo': monedasUsuario.saldo + pago.monto,
            'descripcion': 'Devolución de Big Puntos por no completar la transacción.'
        }
        Monedas.objects.create(**data)
        pago.state = 0
        pago.save()
        # f.write(pago)
        # f.write("se ejecuto \n")

    # f.close()


    