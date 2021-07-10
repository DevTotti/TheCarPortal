from django.db import models
from datetime import datetime
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'



class Merchandise(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=False)
    color_variation = models.CharField(max_length=50, blank=False, null=False)
    new_price = models.DecimalField(max_digits=10, decimal_places=3)
    old_price = models.DecimalField(max_digits=10, decimal_places=3)
    stock = models.PositiveIntegerField(null=False, blank=False)
    type_choices = (
            ('Tees', 'Tees'),
            ('Shorts', 'Shorts'), 
            ('Sweat-Shirt', 'Sweat-Shirt'),
            ('Hoodie', 'Hoodie'),
            ('Face cap', 'Face cap'),
            ('Knapsack', 'Knapsack'),
            ('Socks', 'Socks')
        )

    size_choices = (
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'Xtra-Large'),
            ('XXL','XXtra-Large')
        )

    location_choices = (
            ('Ife', 'Ile-Ife'),
            ('Ibadan', 'Ibadan'),
            ('Lagos', 'Lagos')
        )
    merch_type = models.CharField(max_length=200, null=False, default='', choices=type_choices)
    merch_size = models.CharField(max_length=200, null=False, default='', choices=size_choices)
    location = models.CharField(max_length=200, blank=False, null=False, choices=location_choices, default='Ife')
    in_box = models.CharField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name



class MerchImage(models.Model):
    image = CloudinaryField('image')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    product = models.ForeignKey(Merchandise, default=None, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Auto(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    model = models.CharField(max_length = 200, blank=False)
    color = models.CharField(max_length = 200, blank=False, null=False)
    description = models.TextField(blank=False)
    location_choices = (
            ('Ife', 'Ile-Ife'),
            ('Ibadan', 'Ibadan'),
            ('Lagos', 'Lagos')
        )
    usage_choices = (
            ('UK','UK-Used'),
            ('US','US-Used'),
            ('NIG','Nigerian-Used'),
            ('Other','Other')
        )
    transmission_choice = (
            ('AUTO', 'Authomatic'),
            ('MANUAL','Manual')
        )
    faults = models.TextField(blank=True)
    make = models.CharField(max_length=200, blank=False)
    man_year = models.DateField()
    registered = models.BooleanField(default=False)
    distance_covered = models.IntegerField(null=False)
    gear = models.CharField(max_length=10, blank=False)
    transmission = models.CharField(max_length=200, blank=False, null=False, choices=transmission_choice)
    usage_type = models.CharField(max_length=200, null=False, default='', choices=usage_choices)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=False, null=False, choices=location_choices)


    def __str__(self):
        return self.name


class AutoImage(models.Model):
    video = CloudinaryField('video', blank=True)
    image = CloudinaryField('image')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    product = models.ForeignKey(Auto, default=None, related_name='images', on_delete=models.CASCADE)


    def __str__(self):
        return self.product.name