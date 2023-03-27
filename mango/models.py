from django.db import models
from users.models import CustomUser
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Manga(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.IntegerField(default=2000)
    description = models.TextField(null=False, blank=True)
    genre = models.ManyToManyField(Genre, )
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=False)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


