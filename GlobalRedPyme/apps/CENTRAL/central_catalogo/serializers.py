from rest_framework import serializers

from apps.CENTRAL.central_catalogo.models import Catalogo


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
       	fields = '__all__'

class CatalogoHijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
       	fields = ['_id','nombre','valor']

class CatalogoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
       	fields = ['_id','nombre','tipo','tipoVariable','valor','descripcion','config']


class CatalogoFiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
       	fields = ['_id','nombre','valor']

class CatalogoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
       	fields = ['_id','valor']
    



