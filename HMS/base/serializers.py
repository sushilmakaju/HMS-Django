from rest_framework import serializers
from .models import *

class RoomTypeSerializers(serializers.Serializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializers(serializers.Serializer):
    class Meta:
        model = Room
        fields = '__all__'

class CustomerDetailserializers(serializers.Serializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'

class EmployeeDetailserializers(serializers.Serializer):
    class Meta:
        model = EmployeeDetail
        field = '__all__'

class MenuTypeserializers(serializers.Serializer):
    class Meta:
        model = MenuType
        field = '__all__'

class Foodserializers(serializers.Serializer):
    class Meta:
        model = Food
        field = '__all__'

class Facilitiesserializers(serializers.Serializer):
    class Meta:
        model = Facilities
        field = '__all__'

class Serviceserializers(serializers.Serializer):
    class Meta:
        model = Service
        field = '__all__'

class Billserializers(serializers.Serializer):
    class Meta:
        model = Bill
        field = '__all__'

class Paymentinfoserializers(serializers.Serializer):
    class Meta:
        model = Payment_info
        field = '__all__'