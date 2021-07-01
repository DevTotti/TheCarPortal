from django.shortcuts import render
from .serializers import MerchandiseSerializer, AutoSerializer
from .models import Auto, Merchandise, MerchImage, AutoImage
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class MerchandiseView(RetrieveAPIView):
    queryset = Merchandise.objects.all()
    permission_classes = (AllowAny, IsAuthenticated)

    def get(self, request, **args):
        if not args:
            merch_objects = Merchandise.objects.all()
            merchs = []
            for merch in merch_objects:
                images = MerchImage.objects.filter(product=merch)
                url = str(request.build_absolute_uri()).rstrip("store/")

                data = {
                    "id": merch.id,
                    "name": merch.name,
                    "description": merch.description,
                    "color_variation": merch.color_variation,
                    "new_price": merch.new_price,
                    "old_price": merch.old_price,
                    "stock": merch.stock,
                    "merch_type": merch.merch_type,
                    "merch_size": merch.merch_size,
                    "location": merch.location,
                    "in_box": merch.in_box,
                    "images":[url+'/'+str(img.image) for img in images]
                }

                merchs.append(data)

            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': merchs
            }

            status_ = status.HTTP_200_OK
        
        else:
            merch_id = args['merch_id']
            merch_objects =  Merchandise.objects.get(id=merch_id)
            images = MerchImage.objects.filter(product=merch_objects)
            url = str(request.build_absolute_uri()).rstrip("store/")
            data = {
                "id": merch_objects.id,
                "name": merch_objects.name,
                "description": merch_objects.description,
                "color_variation": merch_objects.color_variation,
                "new_price": merch_objects.new_price,
                "old_price": merch_objects.old_price,
                "stock": merch_objects.stock,
                "merch_type": merch_objects.merch_type,
                "merch_size": merch_objects.merch_size,
                "location": merch_objects.location,
                "in_box": merch_objects.in_box,
                "images":[url+'/'+str(img.image) for img in images]
            }
        
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': data
            }

            status_ = status.HTTP_200_OK

        return Response(response, status_)



class AutoView(RetrieveAPIView):
    queryset = Merchandise.objects.all()
    permission_classes = (AllowAny, IsAuthenticated)

    def get(self, request, **args):
        if not args:
            auto_objects = Auto.objects.all()
            autos = []
            for auto in auto_objects:
                images = AutoImage.objects.filter(product=auto)
                url = str(request.build_absolute_uri()).rstrip("store/")

                data = {
                    "id": auto.id,
                    "name": auto.name,
                    "description": auto.description,
                    "color": auto.color,
                    "model": auto.model,
                    "faults": auto.faults,
                    "make": auto.make,
                    "manufactured": auto.man_year,
                    "registered": auto.registered,
                    "distance_covered": auto.distance_covered,
                    "gear": auto.gear,
                    "transmission": auto.transmission,
                    "usage": auto.usage_type,
                    "location": auto.location,
                    "images":[url+'/'+str(img.image) for img in images]
                }

                autos.append(data)

            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': autos
            }

            status_ = status.HTTP_200_OK
        
        else:
            auto_id = args['auto_id']
            auto_objects =  Auto.objects.get(id=auto_id)
            images = AutoImage.objects.filter(product=auto_objects)
            url = str(request.build_absolute_uri()).rstrip("store/")
            data = {
                "id": auto_objects.id,
                "name": auto_objects.name,
                "description": auto_objects.description,
                "color": auto_objects.color,
                "model": auto_objects.model,
                "faults": auto_objects.faults,
                "make": auto_objects.make,
                "manufactured": auto_objects.man_year,
                "registered": auto_objects.registered,
                "distance_covered": auto_objects.distance_covered,
                "gear": auto_objects.gear,
                "transmission": auto_objects.transmission,
                "usage": auto_objects.usage_type,
                "location": auto_objects.location,
                "images":[url+'/'+str(img.image) for img in images]
            }
        
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': data
            }

            status_ = status.HTTP_200_OK

        return Response(response, status_)