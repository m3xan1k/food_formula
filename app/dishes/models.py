from transliterate import translit

from django.db import models
from django.utils.text import slugify


class Ingredient(models.Model):
    def __str__(self):
        return f"<Ingredient: {self.id}, {self.name}>"

    name = models.TextField()


class DishIngredientWeight(models.Model):
    def __str__(self):
        return f"<DishIngredientWeight: {self.dish.name}, {self.ingredient.name}>"

    dish = models.ForeignKey("Dish", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()


class Dish(models.Model):
    def __str__(self):
        return f"<Dish: {self.id}, {self.name}>"

    name = models.TextField()
    ingredients = models.ManyToManyField(
        "Ingredient",
        related_name="dishes",
        blank=True,
        null=True,
        through=DishIngredientWeight,
    )
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', related_name='dishes', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name='dishes', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name.lower(), 'ru', reversed=True))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "dishes"


class Category(models.Model):
    def __str__(self):
        return f"<Category: {self.id}, {self.name}>"

    name = models.TextField()

    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    def __str__(self):
        return f"<Tag: {self.id}, {self.name}>"

    name = models.TextField()
