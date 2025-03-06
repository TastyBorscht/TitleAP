from rest_framework import serializers

from reviews.models import Review, Comment


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Review
        read_only_fields = ('pub_date',)
        exclude = ('title',)

    def create(self, data):
        if Review.objects.filter(
                title=self.context['title'],
                author=self.context['author']
        ).exists():
            raise serializers.ValidationError(
                'Только 1 отзыв от 1 пользователя.'
            )
        return Review.objects.create(**data)


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        read_only_fields = ('pub_date',)
        exclude = ('title', 'review')
