from django.urls import path
from .views import CarSearchView

urlpatterns = [
    path('search/', CarSearchView.as_view(), name='car-search'),
]
