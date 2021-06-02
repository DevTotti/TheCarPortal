from django.contrib import admin
from .models import Event, EventImg
# Register your models here.
class PostEventImgAdmin(admin.StackedInline):
    model = EventImg

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PostEventImgAdmin]

    class Meta:
        model = Event

@admin.register(EventImg)
class PostEventImgAdmin(admin.ModelAdmin):
    pass