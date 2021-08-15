from django.urls import path
from .views import CarSalesView, InspectionView, OneCarSaleView

urlpatterns = [
    path('carsales/', CarSalesView.as_view()),
    path('inspection/', InspectionView.as_view()),
    path('carsales/<car_id>/', OneCarSaleView.as_view()),

]