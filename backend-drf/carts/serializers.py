from rest_framework import serializers
from .models import CartItem,Cart

class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source="product.name",read_only=True)
    price=serializers.DecimalField(source="product.price",max_digits=10,decimal_places=2,read_only=True)
    tax_percent=serializers.DecimalField(source="product.tax_percent",max_digits=10,decimal_places=2,read_only=True)

    class Meta:
        model=CartItem
        fields="__all__"

        
class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    subtotal=serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)
    tax_amount=serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)
    grand_total=serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)
    class Meta:
        model=Cart
        fields="__all__"



