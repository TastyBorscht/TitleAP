from rest_framework import permissions


class OwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        """
        Пользователям/анонимам доступна страница объекта, если GET
        или пользователь=автор или роль не user.
        """
        if (
            obj.author != request.user
            and (request.method not in permissions.SAFE_METHODS)
            and request.user.user_is_user
        ):
            return False
        return True


class AdminOrSafeMethod(permissions.AllowAny):
    """
    Только админ может создавать/менять/удалять.
    Остальные пользователи и анонимы только смотреть.
    """

    def has_permission(self, request, view):
        if (
            request.user.is_staff is False
            and request.method not in permissions.SAFE_METHODS
        ):
            return False
        return True
