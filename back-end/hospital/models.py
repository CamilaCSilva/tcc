from django.db import models
from ficha_paciente.models import Anamnese

# Create your models here.
class ProfissionaldeSaude(models.Model):
    DOCUMENTOS = ( ('CRM', 'Médico(a)'), ('COREN', 'Enfermeiro(a)'), ('DRF', 'Paramédico(a)'))

    cpf = models.DecimalField(max_digits=11, decimal_places=0, primary_key=True)
    campo_escolha = models.CharField(max_length=5, choices=DOCUMENTOS, blank=False, null=False, default='Paramédico(a)')
    nome_completo = models.CharField(max_length=150)
    celular = models.DecimalField(max_digits=11, decimal_places=0)
    documento_trabalho = models.CharField(max_length=10)
    unidade_de_atendimento = models.CharField(max_length=250)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome_completo
    
class FichaPaciente(models.Model):
    anamnese = models.ForeignKey(Anamnese, on_delete=models.CASCADE, default='0')
    paramedico = models.ForeignKey(ProfissionaldeSaude, on_delete=models.CASCADE, default='0')