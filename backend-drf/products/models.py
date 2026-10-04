from django.db.models import Model
from django.db import models
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_des=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name="Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to='products/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2 ,default=Decimal('0.00'))
    stock = models.IntegerField(default=0)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2 ,default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
