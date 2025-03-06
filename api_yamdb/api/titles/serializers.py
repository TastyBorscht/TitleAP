from rest_framework import serializers

from titles.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description',
            'genre', 'category',
        )


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
        write_only=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        write_only=True
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description',
            'genre', 'category',
        )

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        category = validated_data.pop('category')

        title = Title.objects.create(**validated_data, category=category)
        title.genre.set(genres)

        return title

    def update(self, instance, validated_data):
        genres = validated_data.pop('genre', None)
        category = validated_data.pop('category', None)

        if genres is not None:
            instance.genre.set(genres)

        if category is not None:
            instance.category = category

        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.description = validated_data.get(
            'description', instance.description
        )

        instance.save()

        return instance
