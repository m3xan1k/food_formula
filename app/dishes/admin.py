from django.contrib import admin
from dishes.models import Ingredient, Dish, DishIngredientWeight, Category, Tag


@admin.register(Ingredient, Dish, DishIngredientWeight, Category, Tag)
class DishesAdmin(admin.ModelAdmin):
    pass
