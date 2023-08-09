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