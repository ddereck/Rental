from rest_framework import permissions

class IsProfileComplete(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile_completed()
