from rest_framework import permissions


class IsAdminOrManufacture(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MF' or request.user.is_staff