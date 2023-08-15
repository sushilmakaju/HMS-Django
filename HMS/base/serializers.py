from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoomTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CustomerDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'

class EmployeeDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'


class MenuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        fields = '__all__' 

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class Facilitiesserializers(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'

class Serviceserializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__' 

class Paymentinfoserializers(serializers.ModelSerializer):
    class Meta:
        model = Payment_info
        fields = '__all__'