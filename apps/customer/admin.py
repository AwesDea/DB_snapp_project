from django.contrib import admin

# Register your models here.
from apps.customer.models import Driver, Customer

admin.site.register(Driver)
admin.site.register(Customer)
