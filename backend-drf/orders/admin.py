from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=0
    readonly_fields=['quantity','price','total_price']

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

