
from rest_framework import viewsets
from .models import Maintenance
from .serializers import MaintenanceSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
