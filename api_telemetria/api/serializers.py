from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único da marca do veículo'},
            'nome': {'help_text': 'Nome da marca do veículo'},
        }

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do modelo do veículo'},
            'nome': {'help_text': 'Nome do modelo do veículo'},
        }

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do veículo'},
            'marca': {'help_text': 'Marca do veículo (referência à tabela Marca)'},
            'modelo': {'help_text': 'Modelo do veículo (referência à tabela Modelo)'},
            'ano': {'help_text': 'Ano de fabricação do veículo'},
            'descricao': {'help_text': 'Descrição adicional do veículo'},
            'horimetro': {'help_text': 'Valor atual do horímetro do veículo'},
        }

class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único da medição'},
            'tipo': {'help_text': 'Tipo de medição (ex: temperatura, pressão, etc.)'},
            'unidademedida': {'help_text': 'Unidade de medida da medição (ex: °C, bar, etc.)'},
        }

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único da unidade de medida'},
            'nome': {'help_text': 'Nome da unidade de medida (ex: °C, bar, etc.)'},
        }

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único da medição do veículo'},
            'veiculo': {'help_text': 'Veículo associado à medição (referência à tabela Veiculo)'},
            'medicao': {'help_text': 'Tipo de medição realizada (referência à tabela Medicao)'},
            'valor': {'help_text': 'Valor da medição realizada'},
            'data_hora': {'help_text': 'Data e hora em que a medição foi realizada'},
        }