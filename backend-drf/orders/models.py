from django.utils.text import phone2numeric
from django.db import models
from users.models import User
from products.models import Product
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES=[
        ("PENDING","pending"),
        ("CONFIRMED","confirmed"),
        ("DELIVERED","delivered"),
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2)
    tax_amount=models.DecimalField(max_digits=10,decimal_places=2)
    grand_total=models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    city=models.CharField(max_length=25,blank=True,null=True)
    zip_code=models.CharField(max_length=10,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.email}"
    
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.order}"
    