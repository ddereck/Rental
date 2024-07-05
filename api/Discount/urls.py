from django.urls import path
from .views import DiscountListCreateView, DiscountDetailView

urlpatterns = [
    path('discounts', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail'),
]
