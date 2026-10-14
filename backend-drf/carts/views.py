
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CartItem,Cart
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from products.models import Product
# Create your views here.

class CartListView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        cart,create=Cart.objects.get_or_create(user=request.user)
        serializer=CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        product_id=request.data.get("product_id")
        quantity=request.data.get("quantity")

        if not product_id:
            return Response({"error":"Product ID is required"},status=status.HTTP_400_BAD_REQUEST)

        product=get_object_or_404(Product,id=product_id,is_active=True)
        cart,_=Cart.objects.get_or_create(user=request.user)
        item,created=CartItem.objects.get_or_create(cart=cart,product=product)
        
        if not created:
            item.quantity+=int(quantity)
            item.save()

        serializer=CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class ManageCartItemView(APIView):
    permission_classes=[IsAuthenticated]

    def patch(self,request,item_id):
        if 'change' not in request.data:
            return Response({"error":"change value is req"},status=status.HTTP_400_BAD_REQUEST)
        
        change=int(request.data.get("change"))
        item=get_object_or_404(CartItem,id=item_id,cart__user=request.user)
        product=item.product

        if change>0:
            if item.quantity+change>product.stock:
                return Response({"error":"You can't order more than stock"},status=status.HTTP_400_BAD_REQUEST)

        new_quantiy=item.quantity+change

        if new_quantiy<=0:
            item.delete()
            return Response({"message":"item removed"})

        item.quantity=new_quantiy
        item.save()
        serializer=CartSerializer(item.cart)
        return Response(serializer.data)
    
    def delete(self,request,item_id):
        item=get_object_or_404(CartItem,id=item_id,cart__user=request.user)
        item.delete()
        serializer=CartSerializer(item.cart)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        
        

    
        
