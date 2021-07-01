from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'User registered successfully!'
        }
        
        status_ = status.HTTP_200_OK
        return Response(response, status_)



class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : True,
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully!',
            'token' : serializer.data['token'],
            'username': serializer.data['email']
            }

        status_ = status.HTTP_200_OK

        return Response(response, status=status_)


