# Generated by Django 3.2 on 2024-10-19 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titles.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('rating', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiles', to='titles.category')),
                ('genre', models.ManyToManyField(related_name='genres', through='titles.GenreTitle', to='titles.Genre')),
            ],
            options={
                'ordering': ('-year',),
                'default_related_name': 'tiles',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Оценка')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titles.title', verbose_name='Произведение')),
            ],
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titles.title'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='unique_genre_slug'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='unique_category_slug'),
        ),
        migrations.AddConstraint(
            model_name='title',
            constraint=models.CheckConstraint(check=models.Q(year__lt=2024), name='Неправильное указание года'),
        ),
        migrations.AddConstraint(
            model_name='reviews',
            constraint=models.CheckConstraint(check=models.Q(('score__gte', 1), ('score__lt', 10)), name='Оцените произведение от 1 до 10'),
        ),
    ]
