from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.permissions import AdminOrSafeMethod
from api.titles.mixins import BaseCategoryViewSet
from api.titles.serializers import (TitleSerializer, TitleCreateSerializer,
                                    CategorySerializer, GenreSerializer)
from api.titles.filters import TitleFilter
from titles.models import Title, Category, Genre


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (AdminOrSafeMethod,)
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleCreateSerializer
        return super().get_serializer_class()


class CategoryViewSet(BaseCategoryViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(BaseCategoryViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
