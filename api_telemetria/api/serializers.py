from rest_framework import serializers
from api_telemetria import models 


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    marca_nome = serializers.ReadOnlyField(source='marca.nome')
    modelo_nome = serializers.ReadOnlyField(source='modelo.nome')

    class Meta:
        model = models.Veiculo
        fields = '__all__'


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'


class MedicaoSerializer(serializers.ModelSerializer):
    unidade_nome = serializers.ReadOnlyField(source='unidade_medida.nome')

    class Meta:
        model = models.Medicao
        fields = '__all__'


class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    veiculo_descricao = serializers.ReadOnlyField(source='veiculo.descricao')
    medicao_tipo = serializers.ReadOnlyField(source='medicao.tipo')

    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
