from django.db import models
from orders.models import Order

# Create your models here.


# dev_26
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    imp_uid = models.CharField(max_length=100)
    created_at = models.CharField(auto_now_add=True)
    updated_at = models.CharField(auto_now=True)