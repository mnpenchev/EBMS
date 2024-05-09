from rest_framework import permissions


class IsSelfOrAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj == request.user:
            return True
        return False