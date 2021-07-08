from django.shortcuts import render
from .serializers import EnquirySerializer
from .models import Enquiry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView


# Create your views here.

class EnquiryView(CreateAPIView):
    queryset = Enquiry.objects.all()
    permission_classes = (IsAuthenticated, )
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



class EnquiryGetView(RetrieveAPIView):
    queryset = Enquiry.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = EnquirySerializer

    def get(self, request):
        enq_objects = Enquiry.objects.all()
        message = []
        for enq in enq_objects:
            data = {
                "name": enq.name,
                "email": enq.email,
                "phone": enq.name
            }

            message.append(data)
        
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': message
        }

        status_ = status.HTTP_200_OK
        return Response(response, status_)