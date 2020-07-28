from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_authenticated) and request.user.is_superuser


class IsReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsReferrer(BasePermission):

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_authenticated) and request.user.is_referrer


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_authenticated
        ) and request.user.is_staff


class IsManagerOrReadOnlyPermission(IsManager):

    def has_permission(self, request, view):
        if request.method.upper() in SAFE_METHODS:
            return True
        return super().has_permission(request, view)


class IsReferrerOrManager(BasePermission):

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_authenticated
        ) and (
            request.user.is_staff or
            request.user.is_referrer
        )


class IsCompany(BasePermission):

    def has_permission(self, request, view):
        return request.user and (
            request.user.is_authenticated) and request.user.is_company
