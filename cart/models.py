from django.db import models
from acconts.models import Profile
from shop.models import Shop


class OrderItem(models.Model):
    product = models.OneToOneField(Shop, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def get_cart_total_shipping(self):
        return sum([item.product.price + 15 for item in self.items.all()]) 

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Transaction(models.Model):
    STATUS = (
        ('On Hold', 'on_hold'),
        ('Not Delivered', 'Not Delivered'),
        ('Delivered', 'Delivered')
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.CharField(max_length=100, choices=STATUS, default='Not Delivered')
    purchesed_items = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']

    def get_id(self):
        return self.order_id






        