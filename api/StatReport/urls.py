from django.urls import path
from .views import StatReportListCreateView, StatReportDetailView

urlpatterns = [
    path('', StatReportListCreateView.as_view(), name='stat-report-list-create'),
    path('<int:pk>/', StatReportDetailView.as_view(), name='stat-report-detail'),
]
