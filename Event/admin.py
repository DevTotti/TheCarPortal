from django.contrib import admin
from .models import Event, EventImg, EventVid
# Register your models here.
class PostEventImgAdmin(admin.StackedInline):
    model = EventImg

class PostEventVidAdmin(admin.StackedInline):
    model = EventVid

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PostEventImgAdmin, PostEventVidAdmin]

    class Meta:
        model = Event

@admin.register(EventImg)
class PostEventImgAdmin(admin.ModelAdmin):
    pass

@admin.register(EventVid)
class PostEventVidAdmin(admin.ModelAdmin):
    pass