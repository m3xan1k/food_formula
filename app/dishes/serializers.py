from rest_framework import serializers
from dishes.models import Dish, DishIngredientWeight, Ingredient


class IngredientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name')


class DishIngredientWeightSerializer(serializers.ModelSerializer):
    # ingredient = IngredientNameSerializer

    class Meta:
        model = DishIngredientWeight
        fields = ('id', 'weight', 'ingredient')
        depth = 1


class DishFullSerializer(serializers.ModelSerializer):
    dishingredientweight_set = DishIngredientWeightSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ingredients'] = representation['dishingredientweight_set']
        del representation['dishingredientweight_set']
        return representation

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description',
                  'category', 'tags', 'dishingredientweight_set')

        depth = 1
