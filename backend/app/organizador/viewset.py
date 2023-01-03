from .models import Cliente, Licenca, Condicionante, Medicoes

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ClienteSerializer, LicencaSerializer, CondicionanteSerializer, MedicoesSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class LicencaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows licenças to be viewed or edited.
    """
    queryset = Licenca.objects.all()
    serializer_class = LicencaSerializer
    permission_classes = [permissions.IsAuthenticated]

class CondicionanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows condicionantes to be viewed or edited.
    """
    queryset = Condicionante.objects.all()
    serializer_class = CondicionanteSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows medições to be viewed or edited.
    """
    queryset = Medicoes.objects.all()
    serializer_class = MedicoesSerializer
    permission_classes = [permissions.IsAuthenticated]