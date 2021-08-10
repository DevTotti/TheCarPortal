from django.contrib import admin
from .models import CarSale, CarSaleImage, Inspection, Lead
# Register your models here.


###########################################################

class CarSaleImageAdmin(admin.StackedInline):
    model = CarSaleImage

@admin.register(CarSale)
class CarSaleAdmin(admin.ModelAdmin):
    inlines = [CarSaleImageAdmin]

    class Meta:
        model = CarSale

@admin.register(CarSaleImage)
class CarSaleImageAdmin(admin.ModelAdmin):
    pass

#############################################################
admin.site.register(Inspection)
admin.site.register(Lead)