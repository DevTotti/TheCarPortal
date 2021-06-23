from django.shortcuts import render
from .serializers import EventSerializer
from .models import Event, EventImg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView


# Create your views here.

class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = EventSerializer


    def create(self, request):
        serializer_class = EventSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Event Created'
        }

        status_ = status.HTTP_200_OK
        
        return Response(response, status=status_)


class EventRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request):
        event_objects = Event.objects.all()
        message = []
        for event in event_objects:
            images = EventImg.objects.filter(event=event)
            url = str(request.build_absolute_uri()).rstrip("events/")
            # print(url)
            data = {
                "Title": event.title,
                "Description": event.description,
                "Details": event.full_details,
                "Status": event.status,
                "Date": event.date,
                "Time": event.time,
                "Image": [url+'/static/'+str(img.image) for img in images],
                "Venue": event.venue
            }

            message.append(data)
        
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': message
        }

        status_ = status.HTTP_200_OK
        return Response(response, status_)

