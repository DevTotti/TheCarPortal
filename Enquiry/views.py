from django.shortcuts import render
from .serializers import EnquirySerializer
from .models import Enquiry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView


# Create your views here.

class EventCreateView(CreateAPIView):
    queryset = Enquiry.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = EnquirySerializer


    def create(self, request):
        serializer_class = EnquirySerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Post Created'
        }

        status_ = status.HTTP_200_OK
        
        return Response(response, status=status_)