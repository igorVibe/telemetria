from rest_framework import viewsets
from api_telemetria import models 
from api_telemetria.api import serializers
from drf_yasg.utils import swagger_auto_schema 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from api_telemetria.api.services import processar_csv_medicoes

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Marca",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Marca",
        responses={201: serializers.MarcaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a Marca conforme dados passados, para o ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Marca conforme ID informado",
        responses={200: serializers.MarcaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serializers.ModeloSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Modelo",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Modelo",
        responses={201: serializers.ModeloSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Modelo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o Modelo conforme dados passados, para o ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Modelo conforme ID informado",
        responses={200: serializers.ModeloSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = serializers.VeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Veiculo",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Veiculo",
        responses={201: serializers.VeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Veiculo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o Veiculo conforme dados passados, para o ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Veiculo conforme ID informado",
        responses={200: serializers.VeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadeMedida.objects.all()
    serializer_class = serializers.UnidadeMedidaSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Unidade de Medida",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de Unidade de Medida",
        responses={201: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de Unidade de Medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera a Unidade de Medida conforme dados passados, para o ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de Unidade de Medida conforme ID informado",
        responses={200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicao.objects.all()
    serializer_class = serializers.MedicaoSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Tipos de Medição",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição",
        responses={201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição conforme ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de tipo de medição conforme ID informado",
        responses={200: serializers.MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.MedicaoVeiculo.objects.all()
    serializer_class = serializers.MedicaoVeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Tipos de Medição de Veiculo",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de medição de veiculo",
        responses={201: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de tipo de medição do veiculo conforme ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o tipo de medição do veiculo conforme dados passados, para o ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Apaga o registro de tipo de medição do veiculo conforme ID informado",
        responses={200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class ImportarMedicaoCSVViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UploadCSVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        arquivo = serializer.validated_data["arquivo"]

        try:
            resultado = processar_csv_medicoes(arquivo)
 
            return Response(
                {
                    "mensagem": "Arquivo processado com sucesso.",
                    "resultado": resultado,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {
                    "erro": "Falha ao processar o arquivo.",
                    "detalhe": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        

class medicaoVeiculoTempViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicaoVeiculoTempSerializer
    queryset = models.MedicaoVeiculoTemp.objects.all()
    @swagger_auto_schema(
        operation_description="Retorna Todas as Informações de Medição dos Arquivos",
        responses={200: serializers.MedicaoVeiculoTempSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

