from django.urls import path
from .views import CarSalesView, InspectionView

urlpatterns = [
    path('carsales/', CarSalesView.as_view()),
    path('inspection/', InspectionView.as_view()),
]