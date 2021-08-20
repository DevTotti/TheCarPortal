# from django.contrib import admin
# from .models import CarSale, CarSaleImage, Mechanic, MechanicImage, AutoDiagnostic, AutoDiagnosticImage, Spare, SpareImage
# # Register your models here.


# ###########################################################

# class CarSaleImageAdmin(admin.StackedInline):
#     model = CarSaleImage

# @admin.register(CarSale)
# class CarSaleAdmin(admin.ModelAdmin):
#     inlines = [CarSaleImageAdmin]

#     class Meta:
#         model = CarSale

# @admin.register(CarSaleImage)
# class CarSaleImageAdmin(admin.ModelAdmin):
#     pass


# #############################################################

# class MechanicImageAdmin(admin.StackedInline):
#     model = MechanicImage

# @admin.register(Mechanic)
# class MerchandiseAdmin(admin.ModelAdmin):
#     inlines = [MechanicImageAdmin]

#     class Meta:
#         model = Mechanic

# @admin.register(MechanicImage)
# class MechanicImageAdmin(admin.ModelAdmin):
#     pass



# ###########################################################

# class AutoDiagnosticImageAdmin(admin.StackedInline):
#     model = AutoDiagnosticImage

# @admin.register(AutoDiagnostic)
# class CarSaleAdmin(admin.ModelAdmin):
#     inlines = [AutoDiagnosticImageAdmin]

#     class Meta:
#         model = AutoDiagnostic

# @admin.register(AutoDiagnosticImage)
# class AutoDiagnosticImageAdmin(admin.ModelAdmin):
#     pass


# #############################################################

# class SpareImageAdmin(admin.StackedInline):
#     model = SpareImage

# @admin.register(Spare)
# class MerchandiseAdmin(admin.ModelAdmin):
#     inlines = [SpareImageAdmin]

#     class Meta:
#         model = Spare

# @admin.register(SpareImage)
# class SpareImageAdmin(admin.ModelAdmin):
#     pass