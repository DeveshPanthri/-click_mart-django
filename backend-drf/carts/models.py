from django.db import models
from products.models import Product
# Create your models here.
from django.contrib.auth import get_user_model
from decimal import Decimal

User=get_user_model()

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    @property
    def subtotal(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    def tax_amount(self):
         return sum(item.product.price * item.quantity*Decimal(item.product.tax_percentage)/Decimal("100.0") for item in self.items.all())

    def grand_total(self):
        return self.subtotal+ self.tax_amount()


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_items")
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"