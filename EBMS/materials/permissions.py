from rest_framework import permissions


class IsAdminOrSupply(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MS' or request.user.is_staff