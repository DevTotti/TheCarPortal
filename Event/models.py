from django.db import models
import uuid

# Create your models here.

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    status_choices = [
        ('P', 'Past'),
        ('U', 'Upcoming'),
    ]
    status = models.CharField(max_length=10, default='U', blank=True, choices=status_choices)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    description = models.CharField(max_length=300)
    full_details = models.TextField(blank=True)
    # eventImg = models.ImageField(blank=True)
    venue = models.CharField(max_length=255, blank=False, null=False, default='')


    def __str__(self):
        return self.title


class EventImg(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/media/')
    video = models.FileField(upload_to='static/media/')


    def __str__(self):
        return self.event.title


