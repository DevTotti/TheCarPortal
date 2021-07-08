from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25, unique=True)
    phone = models.CharField(max_length=20, default='', null=True)
    street_no = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    lg = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=False, null=False)
    model = models.CharField(max_length = 200, blank=False)
    color = models.CharField(max_length = 200, blank=False, null=False)
    description = models.TextField(blank=False)
    faults = models.TextField(blank=True)
    registered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email