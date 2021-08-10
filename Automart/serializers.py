from rest_framework import serializers
from .models import CarSale, Inspection


class AutoMartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSale
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'