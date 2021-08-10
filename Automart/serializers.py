from rest_framework import serializers
from .models import CarSale


class AutoMartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSale
        fields = '__all__'


