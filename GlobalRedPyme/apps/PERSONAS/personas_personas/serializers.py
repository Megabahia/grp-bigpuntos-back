from rest_framework import serializers
import json
from .security import encriptar, desencriptar

from .models import (
    Personas, ValidarCuenta
)


class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['identificacion']:
            representation['identificacion'] = desencriptar(eval(representation['identificacion']))
        if representation['nombres']:
            representation['nombres'] = desencriptar(eval(representation['nombres']))
        if representation['apellidos']:
            representation['apellidos'] = desencriptar(eval(representation['apellidos']))
        if representation['nombresCompleto']:
            representation['nombresCompleto'] = desencriptar(eval(representation['nombresCompleto']))
        if representation['genero']:
            representation['genero'] = desencriptar(eval(representation['genero']))
        if representation['fechaNacimiento']:
            representation['fechaNacimiento'] = desencriptar(eval(representation['fechaNacimiento']))
        if representation['edad']:
            representation['edad'] = int(desencriptar(eval(representation['edad'])))
        if representation['ciudad']:
            representation['ciudad'] = desencriptar(eval(representation['ciudad']))
        if representation['provincia']:
            representation['provincia'] = desencriptar(eval(representation['provincia']))
        if representation['pais']:
            representation['pais'] = desencriptar(eval(representation['pais']))
        if representation['direccion']:
            representation['direccion'] = desencriptar(eval(representation['direccion']))
        if representation['email']:
            representation['email'] = desencriptar(eval(representation['email']))
        if representation['emailAdicional']:
            representation['emailAdicional'] = desencriptar(eval(representation['emailAdicional']))
        if representation['telefono']:
            representation['telefono'] = desencriptar(eval(representation['telefono']))
        if representation['whatsapp']:
            representation['whatsapp'] = desencriptar(eval(representation['whatsapp']))
        if representation['referenciaDomicilio']:
            representation['referenciaDomicilio'] = json.loads(desencriptar(eval(representation['referenciaDomicilio'])))
        if representation['ocupacionSolicitante']:
            representation['ocupacionSolicitante'] = json.loads(desencriptar(eval(representation['ocupacionSolicitante'])))
        if representation['referenciasSolicitante']:
            representation['referenciasSolicitante'] = json.loads(desencriptar(eval(representation['referenciasSolicitante'])))
        if representation['ingresosSolicitante']:
            representation['ingresosSolicitante'] = json.loads(desencriptar(eval(representation['ingresosSolicitante'])))
        if representation['gastosSolicitante']:
            representation['gastosSolicitante'] = json.loads(desencriptar(eval(representation['gastosSolicitante'])))
        if representation['estadoCivil']:
            representation['estadoCivil'] = desencriptar(eval(representation['estadoCivil']))
        if representation['tipoIdentificacion']:
            representation['tipoIdentificacion'] = desencriptar(eval(representation['tipoIdentificacion']))
        if representation['tipoPersona']:
            representation['tipoPersona'] = desencriptar(eval(representation['tipoPersona']))
        if representation['celular']:
            representation['celular'] = desencriptar(eval(representation['celular']))
        if representation['codigoUsuario']:
            representation['codigoUsuario'] = desencriptar(eval(representation['codigoUsuario']))
        if representation['garante']:
            representation['garante'] = json.loads(desencriptar(eval(representation['garante'])))
        return representation

    def to_internal_value(self, data):
        if 'identificacion' in data and data.get('identificacion'):
            data['identificacion'] = encriptar(data['identificacion'])
        if 'nombres' in data and data.get('nombres'):
            data['nombres'] = encriptar(data.get('nombres'))
        if 'apellidos' in data and data.get('apellidos'):
            data['apellidos'] = encriptar(data.get('apellidos'))
        if 'nombresCompleto' in data and data.get('nombresCompleto'):
            data['nombresCompleto'] = encriptar(data.get('nombresCompleto'))
        if 'genero' in data and data.get('genero'):
            data['genero'] = encriptar(data.get('genero'))
        if 'fechaNacimiento' in data and data.get('fechaNacimiento'):
            data['fechaNacimiento'] = encriptar(data.get('fechaNacimiento'))
        if 'edad' in data and data.get('edad'):
            data['edad'] = encriptar(str(data.get('edad')))
        if 'ciudad' in data and data.get('ciudad'):
            data['ciudad'] = encriptar(data.get('ciudad'))
        if 'provincia' in data and data.get('provincia'):
            data['provincia'] = encriptar(data.get('provincia'))
        if 'pais' in data and data.get('pais'):
            data['pais'] = encriptar(data.get('pais'))
        if 'direccion' in data and data.get('direccion'):
            data['direccion'] = encriptar(data.get('direccion'))
        if 'email' in data and data.get('email'):
            data['email'] = encriptar(str(data.get('email')))
        if 'emailAdicional' in data and data.get('emailAdicional'):
            data['emailAdicional'] = encriptar(str(data.get('emailAdicional')))
        if 'telefono' in data and data.get('telefono'):
            data['telefono'] = encriptar(data.get('telefono'))
        if 'whatsapp' in data and data.get('whatsapp'):
            data['whatsapp'] = encriptar(data.get('whatsapp'))
        if 'referenciaDomicilio' in data and data.get('referenciaDomicilio'):
            data['referenciaDomicilio'] = encriptar(json.dumps(data.get('referenciaDomicilio')))
        if 'ocupacionSolicitante' in data and data.get('ocupacionSolicitante'):
            data['ocupacionSolicitante'] = encriptar(json.dumps(data.get('ocupacionSolicitante')))
        if 'referenciasSolicitante' in data and data.get('referenciasSolicitante'):
            data['referenciasSolicitante'] = encriptar(json.dumps(data.get('referenciasSolicitante')))
        if 'ingresosSolicitante' in data and data.get('ingresosSolicitante'):
            data['ingresosSolicitante'] = encriptar(json.dumps(data.get('ingresosSolicitante')))
        if 'gastosSolicitante' in data and data.get('gastosSolicitante'):
            data['gastosSolicitante'] = encriptar(json.dumps(data.get('gastosSolicitante')))
        if 'estadoCivil' in data and data.get('estadoCivil'):
            data['estadoCivil'] = encriptar(data.get('estadoCivil'))
        if 'tipoIdentificacion' in data and data.get('tipoIdentificacion'):
            data['tipoIdentificacion'] = encriptar(data.get('tipoIdentificacion'))
        if 'tipoPersona' in data and data.get('tipoPersona'):
            data['tipoPersona'] = encriptar(data.get('tipoPersona'))
        if 'celular' in data and data.get('celular'):
            data['celular'] = encriptar(data.get('celular'))
        if 'codigoUsuario' in data and data.get('codigoUsuario'):
            data['codigoUsuario'] = encriptar(data.get('codigoUsuario'))
        if 'garante' in data and data.get('garante'):
            data['garante'] = encriptar(json.dumps(data.get('garante')))
        return data

class PersonasUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'
        read_only_fields = ['user_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['identificacion']:
            representation['identificacion'] = desencriptar(eval(representation['identificacion']))
        if representation['nombres']:
            representation['nombres'] = desencriptar(eval(representation['nombres']))
        if representation['apellidos']:
            representation['apellidos'] = desencriptar(eval(representation['apellidos']))
        if representation['nombresCompleto']:
            representation['nombresCompleto'] = desencriptar(eval(representation['nombresCompleto']))
        if representation['genero']:
            representation['genero'] = desencriptar(eval(representation['genero']))
        if representation['fechaNacimiento']:
            representation['fechaNacimiento'] = desencriptar(eval(representation['fechaNacimiento']))
        if representation['edad']:
            representation['edad'] = int(desencriptar(eval(representation['edad'])))
        if representation['ciudad']:
            representation['ciudad'] = desencriptar(eval(representation['ciudad']))
        if representation['provincia']:
            representation['provincia'] = desencriptar(eval(representation['provincia']))
        if representation['pais']:
            representation['pais'] = desencriptar(eval(representation['pais']))
        if representation['direccion']:
            representation['direccion'] = desencriptar(eval(representation['direccion']))
        if representation['email']:
            representation['email'] = desencriptar(eval(representation['email']))
        if representation['emailAdicional']:
            representation['emailAdicional'] = desencriptar(eval(representation['emailAdicional']))
        if representation['telefono']:
            representation['telefono'] = desencriptar(eval(representation['telefono']))
        if representation['whatsapp']:
            representation['whatsapp'] = desencriptar(eval(representation['whatsapp']))
        if representation['referenciaDomicilio']:
            representation['referenciaDomicilio'] = json.loads(desencriptar(eval(representation['referenciaDomicilio'])))
        if representation['ocupacionSolicitante']:
            representation['ocupacionSolicitante'] = json.loads(desencriptar(eval(representation['ocupacionSolicitante'])))
        if representation['referenciasSolicitante']:
            representation['referenciasSolicitante'] = json.loads(desencriptar(eval(representation['referenciasSolicitante'])))
        if representation['ingresosSolicitante']:
            representation['ingresosSolicitante'] = json.loads(desencriptar(eval(representation['ingresosSolicitante'])))
        if representation['gastosSolicitante']:
            representation['gastosSolicitante'] = json.loads(desencriptar(eval(representation['gastosSolicitante'])))
        if representation['estadoCivil']:
            representation['estadoCivil'] = desencriptar(eval(representation['estadoCivil']))
        if representation['tipoIdentificacion']:
            representation['tipoIdentificacion'] = desencriptar(eval(representation['tipoIdentificacion']))
        if representation['tipoPersona']:
            representation['tipoPersona'] = desencriptar(eval(representation['tipoPersona']))
        if representation['celular']:
            representation['celular'] = desencriptar(eval(representation['celular']))
        if representation['codigoUsuario']:
            representation['codigoUsuario'] = desencriptar(eval(representation['codigoUsuario']))
        if representation['garante']:
            representation['garante'] = json.loads(desencriptar(eval(representation['garante'])))
        return representation

    def to_internal_value(self, data):
        if 'identificacion' in data and data.get('identificacion'):
            data['identificacion'] = encriptar(data['identificacion'])
        if 'nombres' in data and data.get('nombres'):
            data['nombres'] = encriptar(data.get('nombres'))
        if 'apellidos' in data and data.get('apellidos'):
            data['apellidos'] = encriptar(data.get('apellidos'))
        if 'nombresCompleto' in data and data.get('nombresCompleto'):
            data['nombresCompleto'] = encriptar(data.get('nombresCompleto'))
        if 'genero' in data and data.get('genero'):
            data['genero'] = encriptar(data.get('genero'))
        if 'fechaNacimiento' in data and data.get('fechaNacimiento'):
            data['fechaNacimiento'] = encriptar(data.get('fechaNacimiento'))
        if 'edad' in data and data.get('edad'):
            data['edad'] = encriptar(str(data.get('edad')))
        if 'ciudad' in data and data.get('ciudad'):
            data['ciudad'] = encriptar(data.get('ciudad'))
        if 'provincia' in data and data.get('provincia'):
            data['provincia'] = encriptar(data.get('provincia'))
        if 'pais' in data and data.get('pais'):
            data['pais'] = encriptar(data.get('pais'))
        if 'direccion' in data and data.get('direccion'):
            data['direccion'] = encriptar(data.get('direccion'))
        if 'email' in data and data.get('email'):
            data['email'] = encriptar(str(data.get('email')))
        if 'emailAdicional' in data and data.get('emailAdicional'):
            data['emailAdicional'] = encriptar(str(data.get('emailAdicional')))
        if 'telefono' in data and data.get('telefono'):
            data['telefono'] = encriptar(data.get('telefono'))
        if 'whatsapp' in data and data.get('whatsapp'):
            data['whatsapp'] = encriptar(data.get('whatsapp'))
        if 'referenciaDomicilio' in data and data.get('referenciaDomicilio'):
            data['referenciaDomicilio'] = encriptar(json.dumps(data.get('referenciaDomicilio')))
        if 'ocupacionSolicitante' in data and data.get('ocupacionSolicitante'):
            data['ocupacionSolicitante'] = encriptar(json.dumps(data.get('ocupacionSolicitante')))
        if 'referenciasSolicitante' in data and data.get('referenciasSolicitante'):
            data['referenciasSolicitante'] = encriptar(json.dumps(data.get('referenciasSolicitante')))
        if 'ingresosSolicitante' in data and data.get('ingresosSolicitante'):
            data['ingresosSolicitante'] = encriptar(json.dumps(data.get('ingresosSolicitante')))
        if 'gastosSolicitante' in data and data.get('gastosSolicitante'):
            data['gastosSolicitante'] = encriptar(json.dumps(data.get('gastosSolicitante')))
        if 'estadoCivil' in data and data.get('estadoCivil'):
            data['estadoCivil'] = encriptar(data.get('estadoCivil'))
        if 'tipoIdentificacion' in data and data.get('tipoIdentificacion'):
            data['tipoIdentificacion'] = encriptar(data.get('tipoIdentificacion'))
        if 'tipoPersona' in data and data.get('tipoPersona'):
            data['tipoPersona'] = encriptar(data.get('tipoPersona'))
        if 'celular' in data and data.get('celular'):
            data['celular'] = encriptar(data.get('celular'))
        if 'codigoUsuario' in data and data.get('codigoUsuario'):
            data['codigoUsuario'] = encriptar(data.get('codigoUsuario'))
        if 'garante' in data and data.get('garante'):
            data['garante'] = encriptar(json.dumps(data.get('garante')))
        return data


class PersonasUpdateSinImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        exclude = ['imagen']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['identificacion']:
            representation['identificacion'] = desencriptar(eval(representation['identificacion']))
        if representation['nombres']:
            representation['nombres'] = desencriptar(eval(representation['nombres']))
        if representation['apellidos']:
            representation['apellidos'] = desencriptar(eval(representation['apellidos']))
        if representation['nombresCompleto']:
            representation['nombresCompleto'] = desencriptar(eval(representation['nombresCompleto']))
        if representation['genero']:
            representation['genero'] = desencriptar(eval(representation['genero']))
        if representation['fechaNacimiento']:
            representation['fechaNacimiento'] = desencriptar(eval(representation['fechaNacimiento']))
        if representation['edad']:
            representation['edad'] = int(desencriptar(eval(representation['edad'])))
        if representation['ciudad']:
            representation['ciudad'] = desencriptar(eval(representation['ciudad']))
        if representation['provincia']:
            representation['provincia'] = desencriptar(eval(representation['provincia']))
        if representation['pais']:
            representation['pais'] = desencriptar(eval(representation['pais']))
        if representation['direccion']:
            representation['direccion'] = desencriptar(eval(representation['direccion']))
        if representation['email']:
            representation['email'] = desencriptar(eval(representation['email']))
        if representation['emailAdicional']:
            representation['emailAdicional'] = desencriptar(eval(representation['emailAdicional']))
        if representation['telefono']:
            representation['telefono'] = desencriptar(eval(representation['telefono']))
        if representation['whatsapp']:
            representation['whatsapp'] = desencriptar(eval(representation['whatsapp']))
        if representation['referenciaDomicilio']:
            representation['referenciaDomicilio'] = json.loads(desencriptar(eval(representation['referenciaDomicilio'])))
        if representation['ocupacionSolicitante']:
            representation['ocupacionSolicitante'] = json.loads(desencriptar(eval(representation['ocupacionSolicitante'])))
        if representation['referenciasSolicitante']:
            representation['referenciasSolicitante'] = json.loads(desencriptar(eval(representation['referenciasSolicitante'])))
        if representation['ingresosSolicitante']:
            representation['ingresosSolicitante'] = json.loads(desencriptar(eval(representation['ingresosSolicitante'])))
        if representation['gastosSolicitante']:
            representation['gastosSolicitante'] = json.loads(desencriptar(eval(representation['gastosSolicitante'])))
        if representation['estadoCivil']:
            representation['estadoCivil'] = desencriptar(eval(representation['estadoCivil']))
        if representation['tipoIdentificacion']:
            representation['tipoIdentificacion'] = desencriptar(eval(representation['tipoIdentificacion']))
        if representation['tipoPersona']:
            representation['tipoPersona'] = desencriptar(eval(representation['tipoPersona']))
        if representation['celular']:
            representation['celular'] = desencriptar(eval(representation['celular']))
        if representation['codigoUsuario']:
            representation['codigoUsuario'] = desencriptar(eval(representation['codigoUsuario']))
        if representation['garante']:
            representation['garante'] = json.loads(desencriptar(eval(representation['garante'])))
        return representation

    def to_internal_value(self, data):
        if 'identificacion' in data and data.get('identificacion'):
            data['identificacion'] = encriptar(data['identificacion'])
        if 'nombres' in data and data.get('nombres'):
            data['nombres'] = encriptar(data.get('nombres'))
        if 'apellidos' in data and data.get('apellidos'):
            data['apellidos'] = encriptar(data.get('apellidos'))
        if 'nombresCompleto' in data and data.get('nombresCompleto'):
            data['nombresCompleto'] = encriptar(data.get('nombresCompleto'))
        if 'genero' in data and data.get('genero'):
            data['genero'] = encriptar(data.get('genero'))
        if 'fechaNacimiento' in data and data.get('fechaNacimiento'):
            data['fechaNacimiento'] = encriptar(data.get('fechaNacimiento'))
        if 'edad' in data and data.get('edad'):
            data['edad'] = encriptar(str(data.get('edad')))
        if 'ciudad' in data and data.get('ciudad'):
            data['ciudad'] = encriptar(data.get('ciudad'))
        if 'provincia' in data and data.get('provincia'):
            data['provincia'] = encriptar(data.get('provincia'))
        if 'pais' in data and data.get('pais'):
            data['pais'] = encriptar(data.get('pais'))
        if 'direccion' in data and data.get('direccion'):
            data['direccion'] = encriptar(data.get('direccion'))
        if 'email' in data and data.get('email'):
            data['email'] = encriptar(str(data.get('email')))
        if 'emailAdicional' in data and data.get('emailAdicional'):
            data['emailAdicional'] = encriptar(str(data.get('emailAdicional')))
        if 'telefono' in data and data.get('telefono'):
            data['telefono'] = encriptar(data.get('telefono'))
        if 'whatsapp' in data and data.get('whatsapp'):
            data['whatsapp'] = encriptar(data.get('whatsapp'))
        if 'referenciaDomicilio' in data and data.get('referenciaDomicilio'):
            data['referenciaDomicilio'] = encriptar(json.dumps(data.get('referenciaDomicilio')))
        if 'ocupacionSolicitante' in data and data.get('ocupacionSolicitante'):
            data['ocupacionSolicitante'] = encriptar(json.dumps(data.get('ocupacionSolicitante')))
        if 'referenciasSolicitante' in data and data.get('referenciasSolicitante'):
            data['referenciasSolicitante'] = encriptar(json.dumps(data.get('referenciasSolicitante')))
        if 'ingresosSolicitante' in data and data.get('ingresosSolicitante'):
            data['ingresosSolicitante'] = encriptar(json.dumps(data.get('ingresosSolicitante')))
        if 'gastosSolicitante' in data and data.get('gastosSolicitante'):
            data['gastosSolicitante'] = encriptar(json.dumps(data.get('gastosSolicitante')))
        if 'estadoCivil' in data and data.get('estadoCivil'):
            data['estadoCivil'] = encriptar(data.get('estadoCivil'))
        if 'tipoIdentificacion' in data and data.get('tipoIdentificacion'):
            data['tipoIdentificacion'] = encriptar(data.get('tipoIdentificacion'))
        if 'tipoPersona' in data and data.get('tipoPersona'):
            data['tipoPersona'] = encriptar(data.get('tipoPersona'))
        if 'celular' in data and data.get('celular'):
            data['celular'] = encriptar(data.get('celular'))
        if 'codigoUsuario' in data and data.get('codigoUsuario'):
            data['codigoUsuario'] = encriptar(data.get('codigoUsuario'))
        if 'garante' in data and data.get('garante'):
            data['garante'] = encriptar(json.dumps(data.get('garante')))
        return data


class PersonasImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personas
        fields = ['imagen', 'updated_at']


class ValidarCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidarCuenta
        fields = '__all__'
        read_only_fields = ['_id']


class PersonasSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['_id', 'identificacion', 'nombres', 'apellidos', 'user_id', 'whatsapp']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['identificacion']:
            representation['identificacion'] = desencriptar(eval(representation['identificacion']))
        if representation['nombres']:
            representation['nombres'] = desencriptar(eval(representation['nombres']))
        if representation['apellidos']:
            representation['apellidos'] = desencriptar(eval(representation['apellidos']))
        if representation['nombresCompleto']:
            representation['nombresCompleto'] = desencriptar(eval(representation['nombresCompleto']))
        if representation['genero']:
            representation['genero'] = desencriptar(eval(representation['genero']))
        if representation['fechaNacimiento']:
            representation['fechaNacimiento'] = desencriptar(eval(representation['fechaNacimiento']))
        if representation['edad']:
            representation['edad'] = int(desencriptar(eval(representation['edad'])))
        if representation['ciudad']:
            representation['ciudad'] = desencriptar(eval(representation['ciudad']))
        if representation['provincia']:
            representation['provincia'] = desencriptar(eval(representation['provincia']))
        if representation['pais']:
            representation['pais'] = desencriptar(eval(representation['pais']))
        if representation['direccion']:
            representation['direccion'] = desencriptar(eval(representation['direccion']))
        if representation['email']:
            representation['email'] = desencriptar(eval(representation['email']))
        if representation['emailAdicional']:
            representation['emailAdicional'] = desencriptar(eval(representation['emailAdicional']))
        if representation['telefono']:
            representation['telefono'] = desencriptar(eval(representation['telefono']))
        if representation['whatsapp']:
            representation['whatsapp'] = desencriptar(eval(representation['whatsapp']))
        if representation['referenciaDomicilio']:
            representation['referenciaDomicilio'] = json.loads(desencriptar(eval(representation['referenciaDomicilio'])))
        if representation['ocupacionSolicitante']:
            representation['ocupacionSolicitante'] = json.loads(desencriptar(eval(representation['ocupacionSolicitante'])))
        if representation['referenciasSolicitante']:
            representation['referenciasSolicitante'] = json.loads(desencriptar(eval(representation['referenciasSolicitante'])))
        if representation['ingresosSolicitante']:
            representation['ingresosSolicitante'] = json.loads(desencriptar(eval(representation['ingresosSolicitante'])))
        if representation['gastosSolicitante']:
            representation['gastosSolicitante'] = json.loads(desencriptar(eval(representation['gastosSolicitante'])))
        if representation['estadoCivil']:
            representation['estadoCivil'] = desencriptar(eval(representation['estadoCivil']))
        if representation['tipoIdentificacion']:
            representation['tipoIdentificacion'] = desencriptar(eval(representation['tipoIdentificacion']))
        if representation['tipoPersona']:
            representation['tipoPersona'] = desencriptar(eval(representation['tipoPersona']))
        if representation['celular']:
            representation['celular'] = desencriptar(eval(representation['celular']))
        if representation['codigoUsuario']:
            representation['codigoUsuario'] = desencriptar(eval(representation['codigoUsuario']))
        if representation['garante']:
            representation['garante'] = json.loads(desencriptar(eval(representation['garante'])))
        return representation

    def to_internal_value(self, data):
        if 'identificacion' in data and data.get('identificacion'):
            data['identificacion'] = encriptar(data['identificacion'])
        if 'nombres' in data and data.get('nombres'):
            data['nombres'] = encriptar(data.get('nombres'))
        if 'apellidos' in data and data.get('apellidos'):
            data['apellidos'] = encriptar(data.get('apellidos'))
        if 'nombresCompleto' in data and data.get('nombresCompleto'):
            data['nombresCompleto'] = encriptar(data.get('nombresCompleto'))
        if 'genero' in data and data.get('genero'):
            data['genero'] = encriptar(data.get('genero'))
        if 'fechaNacimiento' in data and data.get('fechaNacimiento'):
            data['fechaNacimiento'] = encriptar(data.get('fechaNacimiento'))
        if 'edad' in data and data.get('edad'):
            data['edad'] = encriptar(str(data.get('edad')))
        if 'ciudad' in data and data.get('ciudad'):
            data['ciudad'] = encriptar(data.get('ciudad'))
        if 'provincia' in data and data.get('provincia'):
            data['provincia'] = encriptar(data.get('provincia'))
        if 'pais' in data and data.get('pais'):
            data['pais'] = encriptar(data.get('pais'))
        if 'direccion' in data and data.get('direccion'):
            data['direccion'] = encriptar(data.get('direccion'))
        if 'email' in data and data.get('email'):
            data['email'] = encriptar(str(data.get('email')))
        if 'emailAdicional' in data and data.get('emailAdicional'):
            data['emailAdicional'] = encriptar(str(data.get('emailAdicional')))
        if 'telefono' in data and data.get('telefono'):
            data['telefono'] = encriptar(data.get('telefono'))
        if 'whatsapp' in data and data.get('whatsapp'):
            data['whatsapp'] = encriptar(data.get('whatsapp'))
        if 'referenciaDomicilio' in data and data.get('referenciaDomicilio'):
            data['referenciaDomicilio'] = encriptar(json.dumps(data.get('referenciaDomicilio')))
        if 'ocupacionSolicitante' in data and data.get('ocupacionSolicitante'):
            data['ocupacionSolicitante'] = encriptar(json.dumps(data.get('ocupacionSolicitante')))
        if 'referenciasSolicitante' in data and data.get('referenciasSolicitante'):
            data['referenciasSolicitante'] = encriptar(json.dumps(data.get('referenciasSolicitante')))
        if 'ingresosSolicitante' in data and data.get('ingresosSolicitante'):
            data['ingresosSolicitante'] = encriptar(json.dumps(data.get('ingresosSolicitante')))
        if 'gastosSolicitante' in data and data.get('gastosSolicitante'):
            data['gastosSolicitante'] = encriptar(json.dumps(data.get('gastosSolicitante')))
        if 'estadoCivil' in data and data.get('estadoCivil'):
            data['estadoCivil'] = encriptar(data.get('estadoCivil'))
        if 'tipoIdentificacion' in data and data.get('tipoIdentificacion'):
            data['tipoIdentificacion'] = encriptar(data.get('tipoIdentificacion'))
        if 'tipoPersona' in data and data.get('tipoPersona'):
            data['tipoPersona'] = encriptar(data.get('tipoPersona'))
        if 'celular' in data and data.get('celular'):
            data['celular'] = encriptar(data.get('celular'))
        if 'codigoUsuario' in data and data.get('codigoUsuario'):
            data['codigoUsuario'] = encriptar(data.get('codigoUsuario'))
        if 'garante' in data and data.get('garante'):
            data['garante'] = encriptar(json.dumps(data.get('garante')))
        return data