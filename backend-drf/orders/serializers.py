from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from users.models import User

class OrderItemSerializer(serializers.ModelSerializer):
    product=serializers.CharField(source="product.name",read_only=True)
    class Meta:
        model=OrderItem
        fields='__all__'



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['created_at','updated_at','user','status']