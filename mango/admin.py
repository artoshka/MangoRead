from django.contrib import admin
from .models import Manga, Genre, Type, Review


admin.site.register(Genre)
admin.site.register(Type)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "manga"]
    search_fields = ["user__username"]
    list_filter = ["manga__name"]
    list_per_page = 10


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "type"]
    list_editable = ["year", "type"]
    search_fields = ["name__istartswith", "type__name"]
    list_filter = ["year", "genre__name"]
    list_per_page = 12

