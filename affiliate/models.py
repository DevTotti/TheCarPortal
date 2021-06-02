from django.db import models
from datetime import datetime
from django.utils import timezone

#####################################################################
class Mechanic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    speciality = models.CharField(max_length=200)
    services =  models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MechanicImage(models.Model):
    video = models.FileField(upload_to='media/')
    image = models.ImageField(upload_to='media/')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    mechanic = models.ForeignKey(Mechanic, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.mechanic.name




####################################################################
class Spare(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    speciality = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpareImage(models.Model):
    video = models.FileField(upload_to='media/')
    image = models.ImageField(upload_to='media/')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    spare = models.ForeignKey(Spare, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.spare.name




#####################################################################
class AutoDiagnostic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    services =  models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AutoDiagnosticImage(models.Model):
    video = models.FileField(upload_to='media/')
    image = models.ImageField(upload_to='media/')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    mechanic = models.ForeignKey(AutoDiagnostic, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.mechanic.name




####################################################################
class CarSale(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)

    car_type = (
            ('Used', 'Used'),
            ('New', 'New')
        )

    typeOfCar = models.CharField(max_length=200, choices=car_type, default='Used')

    def __str__(self):
        return self.name


class CarSaleImage(models.Model):
    video = models.FileField(upload_to='media/')
    image = models.ImageField(upload_to='media/')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    carSale = models.ForeignKey(CarSale, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.carSale.name

########################################################################################