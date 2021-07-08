from django.urls import path
from .views import EnquiryView

urlpatterns = [
    path('', EnquiryView.as_view()),
]