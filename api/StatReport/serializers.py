from rest_framework import serializers
from .models import StatReport

class StatReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatReport
        fields = '__all__'
