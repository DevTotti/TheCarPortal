from django.urls import path
from .views import EventCreateView, EventRetrieveView, EventsRetrieveView

urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('', EventsRetrieveView.as_view()),
    path('get/<event_id>/', EventRetrieveView.as_view()),
]