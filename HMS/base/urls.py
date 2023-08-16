from django.urls import path
from .views import*

urlpatterns = [
    path('roomtype/',RoomTypeView, name='RoomTypeView'),
    path('roomtype/<pk>',RoomTypeDetailsView, name='RoomTypeDetailsView'),
    path('customer/',CustomerDetailsView, name = 'CustomerDetailsView'),
    path('room/<pk>',RoomApiView.as_view(), name='RoomApiView'),
    path('room/',RoomApiView.as_view(), name='RoomApiView'),
    path('login/',login_view, name='login_view'),
    path('register/',register_view, name='register_view'),
    path('menutype/',MenuTypeView, name='MenuTypeView'),
    path('Food/',FoodApiView.as_view(), name='FoodApiView'),
    path('Bill/',BillApiView.as_view(), name='BillApiView'),
    path('payment/',paymentinfoApiView.as_view(), name='paymentinfoApiView'),
    path('Facilities/',FacilitiesApiView.as_view(), name='FacilitiesApiView'),
    path('service/',ServiceApiView.as_view(), name='ServiceApiView'),
    path('employe/',EmployeeViewApi.as_view(), name='EmployeeViewApi'),
    path('food/<pk>',FoodApiView.as_view(), name='FoodApiView'),
   
]
