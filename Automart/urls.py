from django.urls import path
from .views import CarSalesView

urlpatterns = [
    path('carsales/', CarSalesView.as_view()),
]