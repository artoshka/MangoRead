from django_filters import rest_framework as filters

from .models import Manga


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilter(filters.FilterSet):
    genre = CharFilter(field_name='genre__name', lookup_expr='in')
    type = CharFilter(field_name='type__name', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Manga
        fields = ['genre', 'type', "year"]
