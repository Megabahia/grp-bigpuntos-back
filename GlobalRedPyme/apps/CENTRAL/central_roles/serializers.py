from rest_framework import serializers
from apps.CENTRAL.central_roles.models import Roles, RolesUsuarios

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class RolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class RolFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['_id','codigo','nombre']

class ListRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['codigo','nombre','config']

# LISTAR ROLES USUARIO LOGIN
class ListRolesSerializer(serializers.ModelSerializer):
    rol = ListRolSerializer(many=False, read_only=True)
    class Meta:
        model = RolesUsuarios
       	fields = ['_id','rol']

    def to_representation(self, instance):
        data = super(ListRolesSerializer, self).to_representation(instance)
        rol = data.pop('rol')
        if rol['codigo']:
            data['codigo'] = rol['codigo']
        if rol['nombre']:
            data['nombre'] = rol['nombre']
        if rol['config']:
            data['config'] = rol['config']
        return data

class RolesUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesUsuarios
       	fields = '__all__'

    def to_representation(self, instance):
        data = super(RolesUsuarioSerializer, self).to_representation(instance)
        # tomo el campo rol y convierto de OBJECTID a string
        rol = str(data.pop('rol'))
        data.update({"rol": rol})
        # tomo el campo usuario y convierto de OBJECTID a string
        usuario = str(data.pop('usuario'))
        data.update({"usuario": usuario})
        return data

