from django.urls import include, path
from rest_framework import routers

from .constants import VERSION_ONE_PREFIX
from .titles.views import TitleViewSet, CategoryViewSet, GenreViewSet

v1_router = routers.DefaultRouter()
v1_router.register('titles', TitleViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register('genres', GenreViewSet)


urlpatterns = [
    path(f'{VERSION_ONE_PREFIX}/', include(v1_router.urls)),
    path(f'{VERSION_ONE_PREFIX}/', include('api.users.urls')),
    path(f'{VERSION_ONE_PREFIX}/titles/', include('api.reviews.urls')),
]
