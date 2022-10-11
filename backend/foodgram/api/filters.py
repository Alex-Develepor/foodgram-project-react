from django_filters import AllValuesMultipleFilter, rest_framework
from django_filters.widgets import BooleanWidget
from recipe.models import Recipe
from rest_framework.filters import SearchFilter


class ShopFilter(rest_framework.FilterSet):
    shopping_cart = rest_framework.BooleanFilter(widget=BooleanWidget())
    favorited = rest_framework.BooleanFilter(widget=BooleanWidget())
    tag = AllValuesMultipleFilter(field_name='tag__slug')
    author = AllValuesMultipleFilter(field_name='author__id')

    class Meta:
        model = Recipe
        fields = [
            'author__id',
            'tag',
            'favorited',
            'shopping_cart',
        ]


class SearchInt(SearchFilter):
    search_param = 'name'
