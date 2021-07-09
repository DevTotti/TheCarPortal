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


class EventsRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request, **args):
        event_objects = Event.objects.all()
        message = []
        for event in event_objects:
            images = EventImg.objects.filter(event=event)
            url = "http://thecarportal.herokuapp.com/"
            data = {
                "id": event.id,
                "Title": event.title,
                "Description": event.description,
                "Details": event.full_details,
                "Status": event.status,
                "Date": event.date,
                "Time": event.time,
                "Image": [url+str(img.image) for img in images],
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


class EventRetrieveView(RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny, )

    def get(self, request, **args):
        event_objects =  Event.objects.get(id=args['event_id'])
        images = EventImg.objects.filter(event=event_objects)
        url = "http://thecarportal.herokuapp.com/"
        data = {
            "id": event_objects.id,
            "Title": event_objects.title,
            "Description": event_objects.description,
            "Details": event_objects.full_details,
            "Status": event_objects.status,
            "Date": event_objects.date,
            "Time": event_objects.time,
            "Image": [url+str(img.image) for img in images],
            "Venue": event_objects.venue
        }
    
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': data
        }

        status_ = status.HTTP_200_OK
        return Response(response, status_)