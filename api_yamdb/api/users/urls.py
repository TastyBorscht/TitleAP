from django.urls import include, path
from rest_framework import routers

from .views import UsersForAdminViewSet, RegistrationAuthViewSet


user_router = routers.DefaultRouter()
user_router.register('users', UsersForAdminViewSet)
user_router.register(
    'auth', RegistrationAuthViewSet, basename='registration_for_user'
)
urlpatterns = [
    path('', include(user_router.urls)),
]
