from django.contrib import admin

from .models import Category, Genre, GenreTitle, Title


class GenreTitleInline(admin.TabularInline):
    model = GenreTitle
    extra = 1


class TitleAdmin(admin.ModelAdmin):
    inlines = [GenreTitleInline]


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
