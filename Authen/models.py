from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATE_CHOICES = (
    ('Anambra', 'Anambra'),
    ('Delta', 'Delta'),
    ('Enugu', 'Enugu'),
    ('Edo', 'Edo'),
    ('Imo', 'Imo'),
    ('Abia', 'Abia'),
    ('Enonyi', 'Ebonyi'),
    ('Ogun', 'Ogun'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    state = models.CharField(choices=STATE_CHOICES, max_length=200)
    
    def __str__(self):
        return self.name