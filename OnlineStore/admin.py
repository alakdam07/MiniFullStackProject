from django.contrib import admin
from .models import Product
from .models import Offer

# Register your models here.
# to create admin, In terminal type python manage.py createsuperuser


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
