from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import *
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user != None:
        token,_ = Token.objects.get_or_create(user=user)
        # print("Generated Token:", token)
        return Response({'token':token.key})


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
        
@api_view(['GET', 'POST'])
def MenuTypeView(request):
    if request.method == 'GET':
        menu_type_obj = MenuType.objects.all()
        serializer = MenuTypeSerializer(menu_type_obj, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MenuTypeSerializer(data=request.data)
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
            Room_type_detail_obj = RoomType.object.filter(id = pk)
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
    

# @api_view(['GET', 'POST'])

# def room_view(request,pk):
#     if request.method == 'GET':
#         room_objects = Room.objects.filter(room_type = pk)
#         serializer = RoomSerializers(room_objects, many = True)
#         return Response(serializer.data)
     
#     elif request.method == 'POST':
#         serializer = RoomSerializers(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    

class RoomApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type', 'status'] 
    serializer_class = RoomSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, FrontDeskUserPermission]  # Apply the custom permission

    def get(self, request):  # pk parameter is not used, remove it if unnecessary
        room_objects = Room.objects.all()
        filter_obj = self.filter_queryset(room_objects)
        serializer = self.serializer_class(filter_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FoodApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['menutype']
    serializer_class = FoodSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, RestaurantUserPermisssion]  # Apply the custom permission

    def get(self, request):
        food_obj = Food.objects.all()
        filter_obj = self.filter_queryset(food_obj)
        serializer = self.serializer_class(filter_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




    


@api_view(['POST'])

def register_view(request):

    if request.method == 'POST':
        request.data['username'] = 'user'
        
        password = request.data.get("password")
        hash_password = make_password(password)
        request.data['password'] = hash_password
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('user created')
        else:
            return Response(serializer.errors)
    