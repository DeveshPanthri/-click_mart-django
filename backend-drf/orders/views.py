from decouple import config
from .models import Order,OrderItem
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart
from rest_framework.response import Response 
from rest_framework import status
from .serializers import OrderSerializer
from .utils import send_order_notification



# Create your views here.
class PlaceOrderView(APIView):
    #cheack if the user is logged in 
    permission_classes=[IsAuthenticated]

    # cheack if the cart is empty 
    def post(self,request):
        # cart=Cart.objects.get(user=request.user)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        if not cart or cart.items.count()==0:
            return Response({"error":"cart is empty"},status=status.HTTP_400_BAD_REQUEST)

    # create order 
        order=Order.objects.create(
            user=request.user,
            subtotal=cart.subtotal,
            tax_amount=cart.tax_amount(),
            grand_total=cart.grand_total(),
            status="CONFIRMED",
        

    )

    # create orderitems
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                total_price=item.total_price,
            )


    # clear cart 
        cart.items.all().delete()
        # cart.delete()
        # cart.save()

    # send notification email
        send_order_notification(order)
        
            

    # send the response to the frontend
        serializer=OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
