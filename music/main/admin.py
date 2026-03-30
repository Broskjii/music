from django.contrib import admin
from .models import Genre, Track


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name_en", "name_ru", "description")


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration")
    filter_horizontal = ("genres",)
