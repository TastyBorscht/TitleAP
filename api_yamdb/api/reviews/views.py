from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import CommentsSerializer, ReviewsSerializer
from api.permissions import OwnerOrReadOnly
from reviews.models import Review
from titles.models import Title


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    Создание/редактирование/удаление отзывов к произведению.
    Модераторы и админы могут удалять/редактировать чужие.
    """
    serializer_class = ReviewsSerializer
    permission_classes = (OwnerOrReadOnly,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    @property
    def title(self):
        return get_object_or_404(Title, pk=self.kwargs['title_id'])

    def get_serializer_context(self):
        """Дополнительные данные в сериализатор."""
        context = super().get_serializer_context()
        context.update({
            'title': self.title,
            'author': self.request.user
        })
        return context

    def get_queryset(self):
        """Возвращает все отзывы под произведением."""
        return self.title.reviews.all()

    def perform_create(self, serializer):
        """Добавляет автора и связанное с отзывом произведение."""
        serializer.save(
            author=self.request.user,
            title=self.title
        )


class CommentsViewSet(viewsets.ModelViewSet):
    """
    Создание/редактирование/удаление комментариев к отзыву.
    Модераторы и админы могут удалять/редактировать чужие.
    """
    serializer_class = CommentsSerializer
    permission_classes = (OwnerOrReadOnly,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    @property
    def review(self):
        return get_object_or_404(Review, pk=self.kwargs['review_id'])

    @property
    def title(self):
        return get_object_or_404(Title, pk=self.kwargs['title_id'])

    def perform_create(self, serializer):
        """
        Добавляет автора, связанное с отзывом произведение
        и связанный с комментарием отзыв."""
        serializer.save(
            author=self.request.user,
            title=self.title,
            review=self.review
        )

    def get_queryset(self):
        """Возвращает все комметарии под отзывом."""
        return self.title.reviews.get(
            pk=self.kwargs['review_id']
        ).comments.all()
