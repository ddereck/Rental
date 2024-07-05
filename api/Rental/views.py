from rest_framework import viewsets
from .models import Rental
from .serializers import RentalSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
