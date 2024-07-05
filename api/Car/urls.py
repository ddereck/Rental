from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet
from .views import *

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars-list', cars, name='cars-list'),
]
