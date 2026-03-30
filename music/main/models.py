from django.db import models


class Genre(models.Model):
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    name_ru = models.CharField(max_length=100, verbose_name="Name (RU)")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name_ru


class Track(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    duration = models.PositiveIntegerField(verbose_name="Длительность")
    genres = models.ManyToManyField(Genre, related_name="tracks", verbose_name="Жанры")
    audio_file = models.FileField(upload_to='musuc/tracks/', blank=True, null=True)

    def __str__(self):
        return self.title
