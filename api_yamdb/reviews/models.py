from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from titles.models import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name='Произведение'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='автор'
    )
    score = models.IntegerField(
        'оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    text = models.TextField('текст отзыва')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=['title_id', 'author'],
                name='Только 1 отзыв от пользователя'
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name='произведение'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, verbose_name='отзыв'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='автор'
    )
    text = models.TextField(
        verbose_name='текст комментария'
    )
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']
        default_related_name = 'comments'

    def __str__(self):
        return self.text
