from django.contrib import admin
from orders.models import Order, OrderItem

# dev_24
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)