from typing import Any
from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('ms', 'Men Shoes'),
    ('ws', 'Women Shoes'),
    ('el', 'Electronics'),
    ('cl', 'Clothings'),
    ('ph', 'Phones'),
    ('fs', 'Foodstuff'),
    ('cs', 'Cosmetic'),
    ('am', 'Auto mobile'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(default=10)
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    useage = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    
   