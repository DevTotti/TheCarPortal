from django.shortcuts import render
from .serializers import MerchandiseSerializer, AutoSerializer
from .models import Auto, Merchandise
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class MerchandiseCreateView(CreateAPIView):
    queryset = Merchandise.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = MerchandiseSerializer

    def create(self, request):
        serializer_class = MerchandiseSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'New Auto product Created'
        }

        status_ = status.HTTP_200_OK
        
        return Response(response, status=status_)

class MerchandiseRetrieveView(RetrieveAPIView):
    queryset = Merchandise.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request):
        pass