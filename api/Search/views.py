from rest_framework import generics
from rest_framework.filters import SearchFilter
from Car.models import Car
from .serializers import CarSerializer
from rest_framework.permissions import AllowAny

class CarSearchView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = all
