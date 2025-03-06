from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import MethodNotAllowed

from api.permissions import AdminOrSafeMethod


class BaseCategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (AdminOrSafeMethod,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    lookup_field = 'slug'
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(method='GET')
