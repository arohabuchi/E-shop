from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from cart.models import Cart, OrderPlaced, Payment, Wishlist

# Register your models here.

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products','quantity',]
    def products(self,obj):
        link =reverse("admin:App_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link,obj.product.title)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','stripe_order_id','stripe_payment_status','stripe_payment_id','paid']

@admin.register(OrderPlaced)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customers','products','quantity','ordered_date','status', 'payments']
    def products(self,obj):
        link =reverse("admin:App_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link,obj.product.title)

    def customers(self,obj):
        link =reverse("admin:Authen_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link,obj.customer.name)

    def payments(self,obj):
        link =reverse("admin:cart_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link,obj.payment.stripe_payment_id)
