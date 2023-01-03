from django.db import models

from django.urls import reverse

##Validação
from itertools import cycle
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

##Gerando Tokens por sinais
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



LENGTH_CNPJ = 14

def is_cnpj_valido(cnpj: str):
    if len(cnpj) != LENGTH_CNPJ:
        raise ValidationError(
            _('%(cnpj)s is not an even number'),
            params={'value': cnpj},
            )

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        raise ValidationError(
            _('%(cnpj)s error'),
            params={'value': cnpj},
            )

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            raise ValidationError(
            _('%(cnpj)s error'),
            params={'value': cnpj},
            )

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, validators=[is_cnpj_valido])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.nome

    def get_absolute_url(self):
        return f"clientes/{self.cliente_id}"

class Licenca(models.Model):
    class Orgao(models.IntegerChoices):
        SEDET = 1
        SEMARH = 2
        IMA = 3
        IBAMA = 4
        CORPO_DE_BOMBEIROS = 5

    class StatusRenovacao(models.IntegerChoices):
        EM_ANDAMENTO = 1
        NECESSARIO_INICIAR = 2
        NAO_PRECISA = 3
        LICENCA_EM_DIA = 4

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    observacao = models.CharField(max_length=120, blank=True)
    data_de_emissao = models.DateField()
    data_de_entrega = models.DateField()
    arquivo_licenca = models.FileField(upload_to='licencas', blank=True)
    orgao = models.IntegerField(choices=Orgao.choices, null=True)
    status_renovacao = models.IntegerField(choices=StatusRenovacao.choices, null=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.numero


class Condicionante(models.Model):

    class FrequenciaEntrega(models.IntegerChoices):
        MENSAL = 1
        BIMESTRAL = 2
        TRIMESTRAL = 3
        SEMESTRAL = 4
        ANUAL = 5
        UNICA = 6

    licenca = models.ForeignKey(Licenca, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=600)
    numero = models.PositiveSmallIntegerField(default=1)
    data_de_entrega = models.DateField(blank=True)
    frquencia_entrega = models.IntegerField(choices=FrequenciaEntrega.choices, blank=True, null=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"Condicionante {self.numero} da licença {self.licenca}"

class Medicoes(models.Model):

    class Frequencia(models.IntegerChoices):
        DIARIO = 1
        SEMANAL = 2
        QUINZENAL = 3
        MENSAL = 4
        BIMESTRAL = 5
        TRIMESTRAL = 6
        SEMESTRAL = 7
        ANUAL = 8

    condicionante = models.ForeignKey(Condicionante, on_delete=models.CASCADE)
    frequencia = models.IntegerField(choices=Frequencia.choices)
    parametro = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.parametro

    class Meta:
        verbose_name_plural = "Medições"