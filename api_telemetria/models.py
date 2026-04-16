from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    descricao = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField()
    horimetro = models.IntegerField()

    def __str__(self):
        return self.descricao


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Medicao(models.Model):
    tipo = models.CharField(max_length=100)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo



class MedicaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    medicao = models.ForeignKey(Medicao, on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.veiculo} - {self.medicao} - {self.valor}"
    
class MedicaoVeiculoTemp(models.Model):
    veiculoid = models.ForeignKey('Veiculo',on_delete=models.DO_NOTHING)
    medicaoid = models.ForeignKey('Medicao',on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    arquivoid = models.CharField(max_length=256,db_index=True)
