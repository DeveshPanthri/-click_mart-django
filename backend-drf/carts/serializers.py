from rest_framework import serializers
from .models import CartItem,Cart

class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source="product.name",read_only=True)
    class Meta:
        model=CartItem
        fields="__all__"

        
class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True)
    class Meta:
        model=Cart
        fields="__all__"
