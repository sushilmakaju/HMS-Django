from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def RoomTypeView(request):
    if request.method == 'GET':
        room_type_obj = RoomType.objects.all()
        serializer = RoomTypeSerializers(room_type_obj, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RoomTypeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET'])
def CustomerDetailsView(request):
    # queryobj = {'name':'sushil'}
    # return Response(queryobj)
    if request.method == 'GET':
        customer_detail_obj = CustomerDetail.objects.all()
        serializer = CustomerDetailserializers(customer_detail_obj, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerDetailserializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def RoomTypeDetailsView(request,pk):
    if request.method == 'GET':
        try:
            Room_type_detail_obj = RoomType.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = RoomTypeSerializers(Room_type_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            room_type_obj = RoomType.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = RoomTypeSerializers(room_type_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            room_type_obj = RoomType.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        room_type_obj.delete()
        return Response('Data Deleted!')
        

