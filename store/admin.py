from django.contrib import admin

from .models import *


class TypeInLine(admin.StackedInline):
    model = Type
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [TypeInLine]


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Type)

