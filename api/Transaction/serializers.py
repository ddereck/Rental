from rest_framework import serializers
from .models import Transaction
from Rental.serializers import RentalSerializer

class TransactionSerializer(serializers.ModelSerializer):
    rental = RentalSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
