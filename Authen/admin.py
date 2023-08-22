from django.contrib import admin

from .models import Customer

# Register your models here.
@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality','city', 'state', 'zipcode']