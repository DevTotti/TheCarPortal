from django.contrib import admin
from .models import Cart, CartItem, Message
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Message)