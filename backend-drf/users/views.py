from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)