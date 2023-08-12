from django.urls import path
from .views import*

urlpatterns = [
    path('roomtype/',RoomTypeView, name='RoomTypeView'),
    path('roomtype/<pk>',RoomTypeDetailsView, name='RoomTypeDetailsView'),
    path('customer/',CustomerDetailsView, name = 'CustomerDetailsView')
]
