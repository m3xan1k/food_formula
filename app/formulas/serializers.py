from rest_framework import serializers
from formulas.models import Dish, DishIngredientWeight, Ingredient


class DishIngredientWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishIngredientWeight
        exclude = ('dish', 'ingredient')


class IngredientSerializer(serializers.ModelSerializer):
    weight = DishIngredientWeightSerializer

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'weight')
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        details = representation['weight'][0]
        representation['weight'] = details['weight']
        return representation


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'ingredients')

        depth = 1
