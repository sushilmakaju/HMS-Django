from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


User_Type_List = [('Frontdesk', 'Frontdesk'), ('Restaurant', 'Restaurant'), ('Accounting', 'Accounting'), ('Management', 'Management')]
room_status_list = [('Available','Available'),('Unavailable','Unavailable')]
gender_type_list = [('Male', 'Male'), ('Female', 'Female'), ('Others','Others')]
foodtype_list = [('Khajaset', 'khajaset'), ('Stickfood', 'Stickfood'), ('Khanaset', 'Khanaset')]
status_list = [('Paid', 'Paid'), ('Unpaid', 'Unpaid')]
payment_method_list = [('Cash', 'Cash'), ('Fonepay', 'Fonepay')]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, default='User')
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=20, choices=User_Type_List)

    # to login from the email 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class RoomType(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    name = models.CharField(max_length=200)
    room_no = models.IntegerField()
    bed_count = models.IntegerField()
    status = models.CharField(max_length=50, choices= room_status_list)
    room_type = models.ForeignKey(RoomType, on_delete= models.CASCADE)

class CustomerDetail(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices= gender_type_list)
    work = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

class EmployeeDetail(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices= gender_type_list)
    joined_date = models.DateField()
    phone_number = models.IntegerField()
    salary = models.IntegerField()
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class MenuType(models.Model):
    name = models.CharField(max_length=200)

class Food(models.Model):
    name = models.CharField(max_length=200)
    ingridents = models.CharField(max_length=200)
    price = models.IntegerField()
    foodtype = models.CharField(max_length=20, choices= foodtype_list)
    menutype = models.ForeignKey(MenuType, on_delete= models.CASCADE)

class Facilities(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Service(Facilities):
    pass

class Bill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_list)
    paymentdate = models.DateField()
    customer_details = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    
class Payment_info(models.Model):
    paid_amount = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices= payment_method_list)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)