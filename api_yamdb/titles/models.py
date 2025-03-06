import datetime as dt

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg

from .constants import MAX_LEN_NAME, MAX_LEN_SLUG
User = get_user_model()


class Category(models.Model):

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        verbose_name="Категория"
    )
    slug = models.SlugField(
        max_length=MAX_LEN_SLUG,
        unique=True,
        verbose_name="Слаг"
    )

    class Meta:
        ordering = ('slug',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'], name='unique_category_slug'
            )
        ]
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        verbose_name='Жанр'
    )
    slug = models.SlugField(
        max_length=MAX_LEN_SLUG,
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        ordering = ('slug',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'], name='unique_genre_slug'
            )
        ]
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):

    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        through='GenreTitle',
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LEN_NAME
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    @property
    def rating(self):
        return self.reviews.aggregate(Avg('score'))['score__avg'] or None

    class Meta:
        ordering = ('-year',)
        default_related_name = 'titles'
        constraints = [
            models.CheckConstraint(
                check=models.Q(year__lt=dt.datetime.now().year),
                name='Неправильное указание года',
            )
        ]
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):

    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.genre} {self.title}'
