from rest_framework import permissions
from rest_framework.views import Request, View

class VerifyPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )

class VerifyPermissionOrder(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        
        if request.user.is_authenticated == True: 
            if request.method == 'GET':
                return True
            
            if request.method == 'PATCH':
                return True        
        
    