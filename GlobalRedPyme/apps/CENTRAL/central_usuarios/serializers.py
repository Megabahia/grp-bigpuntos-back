from rest_framework import serializers

from apps.CENTRAL.central_usuarios.models import Usuarios
from apps.CENTRAL.central_roles.serializers import RolFiltroSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        exclude = ('password',)


class UsuarioRolSerializer(serializers.ModelSerializer):
    roles = RolFiltroSerializer(many=False, read_only=True)

    class Meta:
        model = Usuarios
        exclude = ('password',)

    def to_representation(self, instance):
        data = super(UsuarioRolSerializer, self).to_representation(instance)
        rol = data.pop('roles')
        for key, val in rol.items():
            data.update({"rol"+key.lower().capitalize(): val})
        return data


class UsuarioCrearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'username', 'email', 'compania',
                  'pais', 'telefono', 'roles', 'whatsapp', 'password', 'estado']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # usuario = Usuarios.objects.create(**validated_data)
        usuario = Usuarios(
            nombres=self.validated_data['nombres'],
            apellidos=self.validated_data['apellidos'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            compania=self.validated_data['compania'],
            pais=self.validated_data['pais'],
            telefono=self.validated_data['telefono'],
            whatsapp=self.validated_data['whatsapp'],
            estado=self.validated_data['estado'],
            roles=self.validated_data['roles']
        )
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
