from django.contrib import admin
from .models import Merchandise, MerchImage, Auto, AutoImage
# Register your models here.


class PostMerchImgAdmin(admin.StackedInline):
    model = MerchImage

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    inlines = [PostMerchImgAdmin]

    class Meta:
        model = Merchandise

@admin.register(MerchImage)
class PostMerchImgAdmin(admin.ModelAdmin):
    pass


class PostAutoImgAdmin(admin.StackedInline):
    model = AutoImage

@admin.register(Auto)
class MerchandiseAdmin(admin.ModelAdmin):
    inlines = [PostAutoImgAdmin]

    class Meta:
        model = Auto

@admin.register(AutoImage)
class PostMerchImgAdmin(admin.ModelAdmin):
    pass