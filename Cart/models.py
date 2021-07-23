from django.db import models
from Store.models import Merchandise
from user.models import User

# Create your models here.
class CartManager(models.Manager):

    def get_existing_or_new(self, request):
        created = False
        cart_id = request.session.get('cart_id')
        if self.get_queryset().filter(id=cart_id, user=request.user, used=False).count() == 1:
            obj = self.model.objects.get(id=cart_id)

        elif self.get_queryset().filter(user=request.user, used=False).count() == 1:
            obj = self.model.objects.get(user=request.user, used=False)
            request.session['cart_id'] = obj.id

        else:
            obj = self.model.objects.create(user=request.user)
            request.session['cart_id'] = obj.id
            created = True

        return obj, created




class Cart(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    delivery = models.CharField(max_length=3000)
    used = models.BooleanField(default=False)
    total = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    trans_id = models.CharField(max_length=300, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return ('TCP-00'+str(self.id)+'-ORD')
    
    # @property
    # def total(self):
    #     total = 0
    #     for item in self.merchs.all():
    #         total += int(item.quantity) * float(item.merch.new_price)
    #         return total

    # @property
    # def total_cart(self):
    #     return sum(item.quantity for item in self.merchs.all())

    

class CartItem(models.Model):
    merch = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='merchs')
    delivered = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            ('merch', 'cart')
        )


    def __str__(self):
        return ('item ' + str(self.id) + ' in cart -> '+str(self.cart))



class Message(models.Model):
    order = models.CharField(max_length=30)
    trans_id = models.CharField(max_length=300, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    failure = models.BooleanField(default=True)
    error = models.CharField(max_length=1000)
    message_body = models.CharField(max_length=10000)

    def __str__(self):
        return self.order