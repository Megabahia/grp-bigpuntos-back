import xmltodict
from datetime import datetime

from rest_framework import serializers


from apps.CENTRAL.central_facturas.models import (
    Facturas, CalificarCompras
)

# Crear factura
class CalificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificarCompras
        fields = '__all__'

    def to_representation(self, instance):
        data = super(CalificacionesSerializer,
                     self).to_representation(instance)
        # tomo el campo factura y convierto de OBJECTID a string
        factura = str(data.pop('factura'))
        data.update({"factura": factura})
        return data


class FacturasSerializer(serializers.ModelSerializer):
    calificaciones = CalificacionesSerializer(read_only=True, many=True)

    class Meta:
        model = Facturas
        fields = '__all__'

class SubirFacturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = ['urlArchivo','user_id']

    # def create(self, validated_data):
    #     extension = str(validated_data['urlArchivo'])
    #     if '.xml' in extension:
    #         archivoXML = dict(xmltodict.parse(validated_data['urlArchivo']))
    #         if 'RespuestaAutorizacionComprobante' in archivoXML.keys():
    #             archivoXML = archivoXML['RespuestaAutorizacionComprobante']['autorizaciones']
            
    #         if 'autorizacion' in archivoXML.keys():
    #             contentido = archivoXML['autorizacion']
    #         else:
    #             contentido = archivoXML['Autorizacion']

            
    #         comprobante = xmltodict.parse(contentido['comprobante'])
            
    #         validated_data['razonSocial'] = comprobante['factura']['infoTributaria']['razonSocial']
    #         validated_data['fechaEmision'] = datetime.strptime(comprobante['factura']['infoFactura']['fechaEmision'],'%d/%m/%Y')
    #         validated_data['importeTotal'] = comprobante['factura']['infoFactura']['importeTotal']
    #         validated_data['numeroFactura'] = contentido['numeroAutorizacion'][24:39]

    #     factura = Facturas.objects.create(**validated_data)
    #     return factura

# Listar factura
class ListFacturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = ['_id', 'created_at', 'numeroFactura',
                  'urlFoto', 'urlArchivo', 'estado']
