from django.urls import path
from .views import*

urlpatterns = [
    path('roomtype/',RoomTypeView, name='RoomTypeView'),
    path('roomtype/<pk>',RoomTypeDetailsView, name='RoomTypeDetailsView'),
    path('customer/',CustomerDetailsView, name = 'CustomerDetailsView'),
    path('room/<pk>',Roomapiview.as_view(), name='room_view'),
    path('room/',Roomapiview.as_view(), name='room_view'),
    path('login/',login_view, name='login_view'),
]
