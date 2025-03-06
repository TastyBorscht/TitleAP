# Проект Я_ЭМ_ДИ_БИ - НУ-КА, ТАЙТЛ ЗАЦЕНИ!

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.


## Исполнители

[Захарова Дарья](https://github.com/dariaz-Git)
[Олег Брюханов](https://github.com/TastyBorscht)

## Как запустить проект

Код на версии Python(3.9.18)
[GCC 11.4.0] on linux

#### Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:dariaz-Git/api_yamdb.git

cd api_yamdb
```
#### Cоздать и активировать виртуальное окружение:
```
python3.9 -m venv venv

. venv/bin/activate
```
#### Установить зависимости из файла requirements.txt:
```
python3.9 -m pip install --upgrade pip

pip install -r requirements.txt
```
#### Выполнить миграции:
```
python3.9 api_yamdb/manage.py migrate
```
#### Запустить проект:
```
python3.9 api_yamdb/manage.py runserver
```

## Тестирование проекта
```
pytest
```

## Примеры запросов:

#### Регистрация
```
http://127.0.0.1:8000/api/v1/auth/signup/
```
#### Получение токена
```
http://127.0.0.1:8000/api/v1/auth/token/
```
#### Страница пользователя
```
http://127.0.0.1:8000/api/v1/users/me/
```
#### Произведения
```
http://127.0.0.1:8000/api/v1/titles/
```
#### Отзывы к произведению
title_id - уникальный номер произведения
```
http://127.0.0.1:8000/api/v1/titles/title_id/reviews/
```
#### Комментарии к отзыву
review_id - уникальный номер произведения
```
http://127.0.0.1:8000/api/v1/titles/title_id/reviews/review_id/comments/
```
#### Категории
```
http://127.0.0.1:8000/api/v1/categories/
```
#### Жанры
```
http://127.0.0.1:8000/api/v1/genres/
```
