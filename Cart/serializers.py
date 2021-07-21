from rest_framework import serializers
from rest_framework.fields import Field

from Store.serializers import MerchandiseSerializer
from user.serializers import UserRegistrationSerializer

from .models import Cart
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    merch = MerchandiseSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'merch', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    merchs = CartItemSerializer(read_only=True, many=True)
    user = UserRegistrationSerializer(read_only=True)

    class Meta:
        model = Cart
        total = Field(source='total')
        total_cart = Field(source='total_cart')
        fields = '__all__'


        