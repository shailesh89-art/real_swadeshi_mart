from django.contrib import admin

# Register your models here.
from .models import product_upload_database,login_details,cart_data,address_data
admin.site.register(product_upload_database)
admin.site.register(login_details)
admin.site.register(cart_data)
admin.site.register(address_data)


