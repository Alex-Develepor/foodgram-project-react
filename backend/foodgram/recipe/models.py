from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название тега',
        max_length=200,
        unique=True
    )
    color_hex = models.CharField(
        verbose_name='Цвет',
        max_length=7,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = 'Tag'
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    units = models.CharField(
        verbose_name='Единицы измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингридиент'
        ordering = ['name']
        constrains = [
            models.UniqueConstraint(
                fields=[
                    'name',
                    'units',
                ],
                name='uniq_for_ingredient'
            )
        ]

        def __str__(self) -> str:
            return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
        related_name='recipes',
    )
    name = models.CharField(
        verbose_name='Название рецепта',
        max_length=200,
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipe_images/',
    )
    text = models.TextField(
        verbose_name='Текстовое описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='recipe.IngredientAmount',
        verbose_name='Ингредиенты',
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tag',
        related_name='recipes',
    )
    cooking_time_min = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[
            validators.MinValueValidator(
                1,
                message='Минимальное время готовки 1 минута'
            )
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return f'{self.name}'


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='В каких рецептах',
        related_name='ingredient',
    )
    ingredients = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Связанные ингредиенты',
        related_name='recipe'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=(
            validators.MinValueValidator(
                1,
                message='Минимальное кол-во ингредиентов 1'
            )
        )
    )

    class Meta:
        verbose_name = 'Кол-во ингредиентов'
        ordering = ['-id']
        constrains = [
            models.UniqueConstraint(
                fields=[
                    'recipe',
                    'ingredients'
                ],
                name='uniq_ingredients_name'
            )
        ]

    def __str__(self) -> str:
        return f'{self.ingredients.name} - {self.amount}'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='cart'
    )

    class Meta:
        verbose_name = 'Корзина'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'user',
                    'recipe'
                ],
                name='unique_cart_user'
            )
        ]


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'user',
                    'recipe'
                ],
                name='unique_user_recipe'
            )
        ]

    def __str__(self):
        return f'{self.user}'
