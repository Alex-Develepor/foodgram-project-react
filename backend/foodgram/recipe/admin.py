from django.contrib.admin import ModelAdmin, register

from .models import Ingredient, Recipe, Tag


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        'name',
    )


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'name',
        'author'
    )
    list_filter = (
        'author',
        'name',
        'tags',
    )
    readonly_fields = (
        'count_favorites',
    )

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.short_description = 'Избранное кол-во'
