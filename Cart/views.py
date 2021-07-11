from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
from Store.models import Merchandise
from .models import Cart, CartItem
from .serializers import CartSerializer


class CartView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        cart_items = request.data.get('cart_items')
        total_cart_price = 0
        for cart_object in cart_items:
            cart_object_id = cart_object['id']
            cart_object_quantity = cart_object['quantity']
            cart_object_total = cart_object['total_price']
            total_cart_price += int(cart_object_total)


            merch_obj = get_object_or_404(Merchandise, id=cart_object_id)
            cart_obj, _ = Cart.objects.get_existing_or_new(request)

        

            if cart_object_quantity <= 0:
                cart_item_qs = CartItem.objects.filter(cart=cart_obj, merch=merch_obj)
                if cart_item_qs.count != 0:
                    cart_item_qs.first().delete()

            else:
                cart_item_obj, created = CartItem.objects.get_or_create(merch=merch_obj, cart=cart_obj)
                cart_item_obj.quantity = cart_object_quantity
                cart_item_obj.price = cart_object_total
                cart_item_obj.save()

        
        request.data['user'] = request.user
        request.data['total'] = total_cart_price
        
        serializer_class = CartSerializer(cart_obj, data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Cart item Created'
        }

        status_ = status.HTTP_200_OK
        
        return Response(response, status=status_)


    def get(self, request, *args, **kwargs):
        resp_data = []
        try:
            cart_obj = Cart.objects.get(user=request.user)
            if cart_obj:
                cart_items = CartItem.objects.filter(cart=cart_obj)
                for item in cart_items:
                    # print(item.merch)
                    data = {
                        "item": item.merch.name,
                        "price": item.merch.new_price,
                        "quantity": item.quantity,
                        "total_item_price": str(item.quantity * item.merch.new_price),
                    }

                    resp_data.append(data)


            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'cart items fetched',
                "data": resp_data
            }
            status_ = status.HTTP_200_OK


        except ObjectDoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Cart empty',
                "data": resp_data
            }
            status_ = status.HTTP_404_NOT_FOUND
        
        return Response(response, status_)


    def patch(self, request, *args, **kwargs):
        print("passing")
        pass



