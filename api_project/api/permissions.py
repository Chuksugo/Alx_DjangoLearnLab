from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only access for unauthenticated users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write access only for owners
        return obj.owner == request.user
