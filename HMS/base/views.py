from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view,authentication_classes, permission_classes
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
    else:
	    return Response('Error')


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
    

class CustomerDetailsViewAPi(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = CustomerDetailserializers


    def get(self,request):
        customer_detail_obj = CustomerDetail.objects.all()
        filter_obj = self.filter_queryset(customer_detail_obj)
        serializer = self.serializer_class(filter_obj, many = True)
        return Response(serializer.data)
   
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        try:
            customer_obj = CustomerDetail.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        customer_obj.delete()
        return Response('Data Deleted!')
    
    def put(self, request, pk):
        try:
            customer_obj = CustomerDetail.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(customer_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
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
    

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])  # You can choose the appropriate authentication class here
# @permission_classes([IsAuthenticated,FrontDeskUserPermission])

# def room_view(request,pk):
#     if request.method == 'GET':
#         room_objects = Room.objects.filter(room_type = pk)
#         serializer = RoomSerializers(room_objects, many = True)
#         return Response(serializer.data)
     

    

class RoomApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type', 'status'] 
    serializer_class = RoomSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, FrontDeskUserPermission]  # Apply the custom permission

    def get(self, request):  
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
        
    def delete(self,request,pk):
        try:
            room_type_obj = Room.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        room_type_obj.delete()
        return Response('Data Deleted!')
    
    def put(self, request, pk):
        try:
            room_type_obj = Room.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(room_type_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FoodApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['menutype', 'foodtype']
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
    
    def delete(self,request,pk):
        try:
            Food_type_obj = Food.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        Food_type_obj.delete()
        return Response('Data Deleted!')
    
    def put(self, request, pk):
        try:
            food_type_obj = Food.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(food_type_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BillApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = BillSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AccountingUserPermission]  # Apply the custom permission

    def get(self, request):
        bill_obj = Bill.objects.all()
        filter_obj = self.filter_queryset(bill_obj)
        serializer = self.serializer_class(filter_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request, pk):
        try:
            bill_obj = Bill.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(bill_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            bill_obj = Bill.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        bill_obj.delete()
        return Response('Data Deleted!')


class paymentinfoApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = Paymentinfoserializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, PaymentinfoUserPermission]  # Apply the custom permission

    def get(self, request):
        payment_obj = Payment_info.objects.all()
        filter_obj = self.filter_queryset(payment_obj)
        serializer = self.serializer_class(filter_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def put(self,request, pk):
        try:
            Paymentinfo_obj = Payment_info.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(Paymentinfo_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            paymentinfo_obj = Payment_info.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        paymentinfo_obj.delete()
        return Response('Data Deleted!')


class FacilitiesApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = Facilitiesserializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ManagementUserPermission]

    def get(self,request):
        facility_obj = Facilities.objects.all()
        filter_obj = self.filter_queryset(facility_obj)
        serializer = self.serializer_class(filter_obj, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request, pk):
        try:
            Facilities_obj = Facilities.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(Facilities_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            Facilities_obj = Facilities.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        Facilities_obj.delete()
        return Response('Data Deleted!')

class ServiceApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = Serviceserializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ManagementUserPermission]

    def get(self,request):
        facility_obj = Service.objects.all()
        filter_obj = self.filter_queryset(facility_obj)
        serializer = self.serializer_class(filter_obj, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request, pk):
        try:
            service_obj = Service.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(service_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            service_obj = Service.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        service_obj.delete()
        return Response('Data Deleted!')
        

class EmployeeViewApi(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'phone_number']
    serializer_class = EmployeeDetailserializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, ManagementUserPermission]
   

    def get(self,request):
        emp_obj = EmployeeDetail.objects.all()
        filter_obj = self.filter_queryset(emp_obj)
        serializer = self.serializer_class(filter_obj, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request, pk):
        try:
            emp_obj = EmployeeDetail.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serializer_class(emp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            emp_obj = EmployeeDetail.objects.filter(id = pk)
        except:
            return Response('Data Not Found!')
        emp_obj.delete()
        return Response('Data Deleted!')

    
   


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
    