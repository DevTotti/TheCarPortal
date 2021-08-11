from django.db import models
from datetime import datetime
from django.utils import timezone
from cloudinary.models import CloudinaryField


####################################################################
class CarSale(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    model = models.CharField(max_length = 200, blank=False)
    exterior_color = models.CharField(max_length = 200, blank=False, null=False)
    interior_color = models.CharField(max_length = 200, blank=False, null=False)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    location_choices = (
            ('Ife', 'Ile-Ife'),
            ('Ibadan', 'Ibadan'),
            ('Lagos', 'Lagos')
        )
    car_type_choices = (
            ('Sedan', 'Sedan'),
            ('SUV', 'SUV'),
            ('Truck', 'Truck')
        )
    drive_train_choices = (
            ('AWD', 'AWD'),
            ('FWD', 'FWD'),
            ('4WD', '4WD')
        )
    engine_type_choices = (
            ('V6', 'V6'),
            ('V12', 'V12'),
            ('V8', 'V8')
        )
    fuel_type_choices = (
            ('Petrol', 'Petrol'),
            ('Diesel', 'Diesel'),
            ('Electric', 'Electric')
        )
    usage_choices = (
            ('Tokunbo','Tokunbo'),
            ('Nigerian-Used','Nigerian-Used')
        )
    transmission_choice = (
            ('AUTO', 'Authomatic'),
            ('MANUAL','Manual')
        )
    type_of_car = models.CharField(max_length=200, null=False, choices=car_type_choices, blank=False)
    engine_type = models.CharField(max_length=200, null=False, choices=engine_type_choices, blank=False)
    drive_train = models.CharField(max_length=200, null=False, choices=drive_train_choices, blank=False)
    fuel_type = models.CharField(max_length=200, null=False, choices=fuel_type_choices, blank=False)
    faults = models.TextField(blank=True)
    make = models.CharField(max_length=200, blank=False)
    man_year = models.DateField()
    registered = models.BooleanField(default=False)
    registration_number = models.CharField(default='', max_length=10, blank=True, null=True)
    distance_covered = models.IntegerField(null=False)
    transmission = models.CharField(max_length=200, blank=False, null=False, choices=transmission_choice)
    usage_type = models.CharField(max_length=200, null=False, default='', choices=usage_choices)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=False, null=False, choices=location_choices)
    video = CloudinaryField(resource_type = "video", blank=True)


    def __str__(self):
        return self.name


class CarSaleImage(models.Model):
    image = CloudinaryField('image')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    product = models.ForeignKey(CarSale, default=None, related_name='images', on_delete=models.CASCADE)


    def __str__(self):
        return self.product.name

########################################################################################


class Inspection(models.Model):
    email = models.CharField(max_length=300, default='', null=True, blank=True)
    phone = models.CharField(max_length=30, default='', null=True, blank=True)
    name = models.CharField(max_length=50, default='', null=True, blank=True)
    responded = models.BooleanField(default=False)


    def __str__(self):
        return self.phone


class Lead(models.Model):
    person = models.ForeignKey(Inspection, on_delete=models.CASCADE, default=None)
    prospect = models.BooleanField(default=False)