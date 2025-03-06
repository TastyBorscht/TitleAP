from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, ReviewsViewSet


reviews_router = routers.DefaultRouter()
reviews_router.register(
    '(?P<title_id>\\d+)/reviews/(?P<review_id>\\d+)/comments',
    CommentsViewSet, basename='comments'
)
reviews_router.register(
    '(?P<title_id>\\d+)/reviews', ReviewsViewSet, basename='reviews'
)

urlpatterns = [
    path('', include(reviews_router.urls)),
]
