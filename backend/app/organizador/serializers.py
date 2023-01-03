from rest_framework import serializers

from .models import Cliente, Licenca, Condicionante, Medicoes

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LicencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenca
        fields = '__all__'

class CondicionanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condicionante
        fields = '__all__'

class MedicoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicoes
        fields = '__all__'