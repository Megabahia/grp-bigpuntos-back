from rest_framework import serializers

from .models import (
    Empresas, EmpresasConvenio, Empleados
)


class EmpresasSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = '__all__'
        read_only_fields = ['_id']


class EmpresasInfoBasicaSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = ['_id', 'nombreEmpresa', 'imagen', 'nombreComercial']


class EmpresasFiltroSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = ['_id', 'nombreEmpresa', 'ruc', 'tipoEmpresa', 'tipoCategoria']


class EmpresasFiltroIfisSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = ['_id', 'nombreEmpresa', 'nombreComercial', 'tipoCategoria', 'ruc', 'imagen']


class EmpresasConvenioCreateSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla EmpresasConvenio
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = EmpresasConvenio
        fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(EmpresasConvenioCreateSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        convenio = str(data.pop('convenio'))
        data.update({"convenio": convenio})
        return data


class EmpresasConvenioSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla EmpresasConvenio
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = EmpresasConvenio
        fields = ['convenio']

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(EmpresasConvenioSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        convenio = data.pop('convenio')
        empresa = Empresas.objects.filter(_id=convenio, state=1).first()
        data.update(EmpresasSerializer(empresa).data)
        return data


class EmpresasLogosSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = ['imagen']


class EmpleadosSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empleados
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empleados
        fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(EmpleadosSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        empresa = data.pop('empresa')
        empresa = Empresas.objects.filter(_id=empresa, state=1).first()
        if empresa is not None:
            data['ruc'] = (EmpresasSerializer(empresa).data['ruc'])
            data['nombreComercial'] = (EmpresasSerializer(empresa).data['nombreComercial'])
        return data


class EmpresasImagenB64Serialazer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Empresas
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Empresas
        fields = '__all__'

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(EmpresasImagenB64Serialazer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        # imagen = data.pop('imagen')
        # if imagen:
        #
        #     # Obtener la imagen de la URL
        #
        #     response = requests.get(imagen)
        #
        #     # Codificar la imagen en Base64
        #
        #     imagen_base64 = base64.b64encode(response.content).decode('utf-8')
        #     data['imagen'] = f"data:image/png;base64,{imagen_base64}"
        #
        #     # 'data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAAyAAAAMgCAMAAADsrvZaAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJBQTFRF+tcAAEZsg6W2wdLbvrQxPHeR8PT2AFJ10d7korvJJWqI4OntAl9/YY6kgpBIssfSPWxb+tolkrHA//zy/OFbAFBoT4Kbcpmt/OuV7M4WoKI9/vfYYX5S+99M/OZ53MUg/fXLB1pj/fCw/vrl+9w6zrwq/ORqJmNg/O6j/emH/fK+cYdOT3VXkZlDsKw4////IY4+CQAAADB0Uk5T//////////////////////////////////////////////////////////////8AYqXQeAAAJgtJREFUeNrsnel62joQQL3EBrOEQAmQnWZfmvD+b3ebNL1lsa2RLHk952c/GoysY81II9nbAEAmHk0AgCAACAKAIAAIAoAgAAgCgCAACAKAIACAIAAIAoAgAAgCgCAACAKAIAAIAoAgAAgCAAgCgCAACAKAIAAIAoAgAAgCgCAACAIACAKAIAAIAoAgAAgCgCAACAKAIAAIAoAgAIAgAAgCgCAACAKAIAAIAoAgAAgCgCAAgCAACAKAIAAIAoAgAAgCgCAACAKAIAAIAgAIAoAgAAgCgCAACAKAIAAIAoAgAAgCAAgCgCAACAKAIAAIAoAgAAgCgCAACAKAIACAIAAIAoAgAAgCgCAACAKAIAAIAoAgAAhCEwAgCACCACAIAIIAIAgAggAgCACCACAIACAIAIIAIAgAggAgCACCACAIAIIAIAgAggAAggAgCACCACAIAIIAIAgAggAgCACCAACCACAIAIIAIAgAggAgCACCACAIAIIAIAgAIAgAggAgCACCACAIAIIAIAgAggAgCAAgCACCACAIAIIAIAgAggAgCACCACAIAIIAAIIAIAgAggAgCACCACAIAIIAIAgAggAAggAgCACCACAIAIIAIAgAggAgCACCACAIACAIAIIAIAgAgrSdi/X6ebVazfd4+f1vr+s17YMgHWX9urqeX3lK7uePq9v1DxoMQTqjxvPLfOrpMr9eoQmCtD2eer6+8gpw/4glCNLWgWM196xw9fKKJAjSrpHDlhxIgiBt48ft49Rzwfz5jtZFkGZz9zz3HHL/ckEbI0hz7bjynIMjCNLQyGru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'
        #     # 'data:image/jpeg;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPEVycm9yPjxDb2RlPkFjY2Vzc0RlbmllZDwvQ29kZT48TWVzc2FnZT5BY2Nlc3MgRGVuaWVkPC9NZXNzYWdlPjxSZXF1ZXN0SWQ+TkM3RUQ2Tk4zODQ4NUhONzwvUmVxdWVzdElkPjxIb3N0SWQ+NHY4dms2WmVTL3dvSno4Y0ptdFVKVHlsYUNoZHZQK2hCd2VFTm5UTDhFQ2pSRU5vYTgxVldvUElWSXdGMmV2SlNSenpxMHRyVnBBPTwvSG9zdElkPjwvRXJyb3I+'
        # else:
        #     data['imagen'] = 'data:image/jpeg;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPEVycm9yPjxDb2RlPkFjY2Vzc0RlbmllZDwvQ29kZT48TWVzc2FnZT5BY2Nlc3MgRGVuaWVkPC9NZXNzYWdlPjxSZXF1ZXN0SWQ+TkM3RUQ2Tk4zODQ4NUhONzwvUmVxdWVzdElkPjxIb3N0SWQ+NHY4dms2WmVTL3dvSno4Y0ptdFVKVHlsYUNoZHZQK2hCd2VFTm5UTDhFQ2pSRU5vYTgxVldvUElWSXdGMmV2SlNSenpxMHRyVnBBPTwvSG9zdElkPjwvRXJyb3I+'
        return data
