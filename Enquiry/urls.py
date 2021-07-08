from django.urls import path
from .views import EnquiryView, EnquiryGetView

urlpatterns = [
    path('', EnquiryView.as_view()),
    path('all/', EnquiryGetView.as_view()),
]