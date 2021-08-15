from django.shortcuts import render
from .serializers import AutoMartSerializer, InspectionSerializer
from .models import CarSale, CarSaleImage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView
# Create your views here.
img_url = "https://res.cloudinary.com/the-car-portal/image/upload/"
vid_url = "https://res.cloudinary.com/the-car-portal/video/upload/"

class CarSalesView(RetrieveAPIView):
    queryset = CarSale.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request, **args):
        carsales_objects = CarSale.objects.all()
        message = []
        for car in carsales_objects:
            images = CarSaleImage.objects.filter(product=car)
            data = {
                "id": car.id,
                "name": car.name,
                "model": car.model,
                "exterior_color": car.exterior_color,
                "interior_color": car.interior_color,
                "description": car.description,
                "price": car.price,
                "style": car.type_of_car,
                "engine_type": car.engine_type,
                "drive_train": car.drive_train,
                "fuel": car.fuel_type,
                "faults": car.faults,
                "make": car.make,
                "man_year": car.man_year,
                "registered": car.registered,
                "distance": car.distance_covered,
                "transmission": car.transmission,
                "usage": car.usage_type,
                "location": car.location,
                "images": [img_url+str(img.image) for img in images],
                "video": vid_url+str(car.video)
            }

            message.append(data)


        
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': message
        }

        status_ = status.HTTP_200_OK
        return Response(response, status_)


class OneCarSaleView(RetrieveAPIView):
    queryset = CarSale.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request, **args):
        car = CarSale.objects.get(id=args['car_id'])
        message = []
        
        images = CarSaleImage.objects.filter(product=car)
        data = {
            "id": car.id,
            "name": car.name,
            "model": car.model,
            "exterior_color": car.exterior_color,
            "interior_color": car.interior_color,
            "description": car.description,
            "price": car.price,
            "style": car.type_of_car,
            "engine_type": car.engine_type,
            "drive_train": car.drive_train,
            "fuel": car.fuel_type,
            "faults": car.faults,
            "make": car.make,
            "man_year": car.man_year,
            "registered": car.registered,
            "distance": car.distance_covered,
            "transmission": car.transmission,
            "usage": car.usage_type,
            "location": car.location,
            "images": [img_url+str(img.image) for img in images],
            "video": vid_url+str(car.video)
        }
        
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': data
        }

        status_ = status.HTTP_200_OK
        return Response(response, status_)


class InspectionView(CreateAPIView):
    queryset = CarSale.objects.all()
    permission_classes = (AllowAny, )

    def post(self, request, **args):
        if request.data:
            serializer_class = InspectionSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Inspection created'
            }

            status_ = status.HTTP_200_OK

        else:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Error creating inspection'
            }

            status_ = status.HTTP_400_BAD_REQUEST

        
        return Response(response, status=status_)