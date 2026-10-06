from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CartItem,Cart
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
# Create your views here.

class CartListView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        cart,create=Cart.objects.get_or_create(user=request.user)
        serializer=CartSerializer(cart)
        return Response(serializer.data)


