from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=500)
    stockleft = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_time = models.DateTimeField(default=timezone.now)
    
    
    