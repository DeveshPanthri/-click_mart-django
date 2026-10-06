from django.db import models
from products.models import Product
# Create your models here.
from django.contrib.auth import get_user_model

User=get_user_model()

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_items")
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"