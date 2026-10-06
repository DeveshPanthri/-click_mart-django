from django.contrib import admin
from .models import Cart,CartItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display=["cart","product","quantity"]


admin.site.register(Cart)
admin.site.register(CartItem,CartItemAdmin)
