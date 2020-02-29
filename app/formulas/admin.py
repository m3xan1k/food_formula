from django.contrib import admin
from formulas.models import Ingredient, Dish, DishIngredientWeight


@admin.register(Ingredient, Dish, DishIngredientWeight)
class FormulasAdmin(admin.ModelAdmin):
    pass
