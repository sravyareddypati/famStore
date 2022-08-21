from django.contrib import admin
from home.models import Contact
from home.models import Product
from home.models import Orders
from home.models import OrderUpdate
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)