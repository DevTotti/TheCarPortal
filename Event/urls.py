from django.urls import path
from .views import EventCreateView, EventRetrieveView

urlpatterns = [
    path('create/', EventCreateView.as_view()),
    path('', EventRetrieveView.as_view()),
]