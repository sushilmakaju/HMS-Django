from rest_framework import serializers
from .models import *

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
        field = '__all__'

class MenuTypeserializers(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        field = '__all__'

class Foodserializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        field = '__all__'

class Facilitiesserializers(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        field = '__all__'

class Serviceserializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        field = '__all__'

class Billserializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        field = '__all__'

class Paymentinfoserializers(serializers.ModelSerializer):
    class Meta:
        model = Payment_info
        field = '__all__'