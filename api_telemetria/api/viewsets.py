from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api import serializers
    


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serializers.ModeloSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = serializers.VeiculoSerializer


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadeMedida.objects.all()
    serializer_class = serializers.UnidadeMedidaSerializer


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicao.objects.all()
    serializer_class = serializers.MedicaoSerializer


class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.MedicaoVeiculo.objects.all()
    serializer_class = serializers.MedicaoVeiculoSerializer
