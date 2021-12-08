from rest_framework import serializers

from apps.CENTRAL.central_usuarios.models import Usuarios, UsuariosEmpresas
from apps.CENTRAL.central_roles.models import RolesUsuarios
from apps.CENTRAL.central_roles.serializers import RolFiltroSerializer, ListRolSerializer
from apps.CORP.corp_empresas.models import Empresas
from apps.CORP.corp_empresas.serializers import EmpresasSerializer
# ObjectId
from bson import ObjectId

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        exclude = ('password',)
    
    def to_representation(self, instance):
        data = super(UsuarioSerializer, self).to_representation(instance)
        # convierto a str tipoUsuario
        tipoUsuario = str(data.pop('tipoUsuario'))
        data.update({"tipoUsuario": tipoUsuario})
        return data


class UsuarioRolSerializer(serializers.ModelSerializer):
    roles = RolFiltroSerializer(many=False, read_only=True)

    class Meta:
        model = Usuarios
        exclude = ('password',)

    def to_representation(self, instance):
        data = super(UsuarioRolSerializer, self).to_representation(instance)
        # rol = data.pop('roles')
        # for key, val in rol.items():
        #     data.update({"rol"+key.lower().capitalize(): val})
        if instance.tipoUsuario != None:
            tipoUsuario = str(instance.tipoUsuario.nombre)
            data.update({"tipoUsuario": tipoUsuario})
        return data

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
    roles = RolFiltroSerializer(many=False, read_only=True)

    class Meta:
        model = Usuarios
        exclude = ('password',)

    def to_representation(self, instance):
        data = super(UsuarioEmpresaSerializer, self).to_representation(instance)
        usuarioEmpresa = UsuariosEmpresas.objects.filter(usuario=instance._id).first()
        rolesUsuarios = RolesUsuarios.objects.filter(usuario=instance._id)
        if rolesUsuarios != None:
            for rolUsuario in rolesUsuarios:
                data.update({"rol"+rolUsuario.rol.nombre: ListRolSerializer(rolUsuario.rol).data})
        if usuarioEmpresa != None:
            empresa = Empresas.objects.filter(pk=ObjectId(usuarioEmpresa.empresa_id),state=1).first()
            data.update({"empresa": EmpresasSerializer(empresa).data})
        if instance.tipoUsuario != None:
            tipoUsuario = str(instance.tipoUsuario.nombre)
            data.update({"tipoUsuario": tipoUsuario})
        return data


class UsuarioCrearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields = ['email', 'password', 'estado','tipoUsuario']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def to_representation(self, instance):
        data = super(UsuarioCrearSerializer, self).to_representation(instance)
        # convierto a str tipoUsuario
        tipoUsuario = str(data.pop('tipoUsuario'))
        data.update({"tipoUsuario": tipoUsuario})
        return data

    def create(self, validated_data):
        usuario = Usuarios.objects.create(**validated_data)
        password = self.validated_data['password']
        usuario.set_password(password)
        usuario.save()

        return usuario


class UsuarioImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['imagen', 'updated_at']


class UsuarioFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['_id', 'nombres', 'apellidos']

    def to_representation(self, instance):
        data = super(UsuarioFiltroSerializer, self).to_representation(instance)
        # tomo y uno los nombres y apellidos y los asigno a la data como nombre
        nombreCompleto = str(data.pop('nombres'))+" " + \
            str(data.pop('apellidos'))
        data.update({"nombre": nombreCompleto})
        return data
