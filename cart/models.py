from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from Authen.models import Customer

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField( default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    stripe_order_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_status = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id = models.CharField(max_length=100,blank=True, null=True)
    paid = models.BooleanField(default=False)

Status_choices = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=60, choices=Status_choices, default='pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    tracking_no= models.CharField(max_length=10, blank=True, null=True)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
        

class Wishlist(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE) 
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        
