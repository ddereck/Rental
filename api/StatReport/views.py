from rest_framework import generics
from .models import StatReport
from .serializers import StatReportSerializer
from rest_framework.permissions import IsAuthenticated

class StatReportListCreateView(generics.ListCreateAPIView):
    queryset = StatReport.objects.all()
    serializer_class = StatReportSerializer
    permission_classes = [IsAuthenticated]

class StatReportDetailView(generics.RetrieveAPIView):
    queryset = StatReport.objects.all()
    serializer_class = StatReportSerializer
    permission_classes = [IsAuthenticated]
