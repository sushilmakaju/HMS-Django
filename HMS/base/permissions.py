from rest_framework.permissions import BasePermission

class FrontDeskUserPermission(BasePermission):

    def has_permission(self, request,view):
        if request.user.user_type == 'Frontdesk':
            return True

class RestaurantUserPermisssion(BasePermission):
    def has_permission(self, request,view):
        if request.user.user_type == 'Restaurant':
            return True

class AccountingUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'Account':
            return True

class PaymentinfoUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'Account':
            return True

class ManagementUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'Management':
            return True



        
