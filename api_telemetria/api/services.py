import csv
import os
import uuid
from decimal import Decimal
from datetime import datetime

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction, connection

from api_telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao

def executar_procedure_pos_importacao(arquivoid):
    """
    Executa a procedure no banco.
    Ajuste o nome da procedure e os parâmetros conforme sua necessidade.
    """
    with connection.cursor() as cursor:
        # Exemplo sem parâmetro:
        # cursor.callproc("sua_procedure")

        # Exemplo passando arquivoid:
        cursor.callproc("processa_arquivo", [arquivoid])


def processar_csv_medicoes(arquivo):
    # Gera um ID único para identificar essa importação
    arquivoid = str(uuid.uuid4())

    # Define a pasta onde os arquivos serão salvos
    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes_medicao")
    # Cria a pasta caso ela não exista
    os.makedirs(pasta_destino, exist_ok=True)

    # Cria um nome único para o arquivo (evita sobrescrever arquivos)
    nome_salvo = f"{arquivoid}_{arquivo.name}"
    # Inicializa o sistema de armazenamento do Django
    fs = FileSystemStorage(location=pasta_destino)
    # Salva o arquivo na pasta definida
    nome_arquivo_salvo = fs.save(nome_salvo, arquivo)
    # Monta o caminho completo do arquivo salvo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo_salvo)

    # Inicializa variáveis de controle
    total_linhas_arquivo = 0  # total de linhas lidas no CSV
    erros = []  # lista para armazenar erros por linha
    linhas_para_inserir = []  # lista de objetos válidos para inserir no banco

    # Cria cache em memória dos veículos e medições (melhora performance)
    veiculos_cache = {v.id: v for v in Veiculo.objects.all()}
    medicoes_cache = {m.id: m for m in Medicao.objects.all()}

    # Abre o arquivo CSV para leitura
    with open(caminho_completo, mode="r", encoding="utf-8-sig", newline="") as f:
        # Lê o CSV como dicionário (cada linha vira um dict)
        reader = csv.DictReader(f, delimiter=';')

        # Define os campos obrigatórios do CSV
        campos_esperados = {"veiculoid", "medicaoid", "data", "valor"}

        # Verifica se existe cabeçalho no arquivo
        if not reader.fieldnames:
            raise Exception("O CSV não possui cabeçalho.")

        # Verifica se o cabeçalho contém os campos esperados
        if not campos_esperados.issubset(set(reader.fieldnames)):
            raise Exception(
                f"Cabeçalho inválido. Esperado: {list(campos_esperados)}. Recebido: {reader.fieldnames}"
            )

        # Percorre cada linha do CSV (começando da linha 2 por causa do cabeçalho)
        for numero_linha, row in enumerate(reader, start=2):
            total_linhas_arquivo += 1  # incrementa contador de linhas

            try:
                # Converte os IDs para inteiro
                id_veiculo = int(row["veiculoid"])
                id_medicao = int(row["medicaoid"])

                # Busca o veículo no cache
                veiculo = veiculos_cache.get(id_veiculo)
                if not veiculo:
                    raise Exception(f"Veículo {id_veiculo} não encontrado.")

                # Busca a medição no cache
                medicao = medicoes_cache.get(id_medicao)
                if not medicao:
                    raise Exception(f"Medição {id_medicao} não encontrada.")

                # Converte a data para datetime
                data_convertida = datetime.strptime(
                    row["data"].strip(),
                    "%Y-%m-%d %H:%M:%S"
                )

                # Converte o valor para Decimal (precisão financeira)
                valor_convertido = Decimal(row["valor"].strip())

                # Cria o objeto temporário e adiciona na lista
                linhas_para_inserir.append(
                    MedicaoVeiculoTemp(
                        veiculoid=veiculo,
                        medicaoid=medicao,
                        data=data_convertida,
                        valor=valor_convertido,
                        arquivoid=arquivoid
                    )
                )

            except Exception as e:
                # Se ocorrer erro, armazena a linha e o erro
                erros.append({
                    "linha": numero_linha,
                    "erro": str(e)
                })

    # Calcula total de linhas válidas
    total_linhas_validas = len(linhas_para_inserir)

    # Inicia uma transação no banco (tudo ou nada)
    with transaction.atomic():
        # Insere os dados em lote (melhor performance)
        if linhas_para_inserir:
            MedicaoVeiculoTemp.objects.bulk_create(linhas_para_inserir, batch_size=1000)

        # Conta quantas linhas foram realmente inseridas
        total_linhas_importadas = MedicaoVeiculoTemp.objects.filter(
            arquivoid=arquivoid
        ).count()

        # Verifica se a quantidade esperada bate com a inserida
        quantidades_conferem = total_linhas_validas == total_linhas_importadas

        # Se tudo estiver correto, executa a procedure pós-importação
        if quantidades_conferem:
           executar_procedure_pos_importacao(arquivoid)
        else:
            # Caso contrário, remove os dados inseridos (rollback manual)
            MedicaoVeiculoTemp.objects.filter(arquivoid=arquivoid).delete()

    # Retorna um resumo da importação
    return {
        "arquivoid": arquivoid,
        "arquivo_salvo": nome_arquivo_salvo,
        "caminho": caminho_completo,
        "total_linhas_arquivo": total_linhas_arquivo,
        "total_linhas_importadas": total_linhas_importadas,
        "quantidades_conferem": total_linhas_arquivo == total_linhas_importadas,
        "erros": erros
    }