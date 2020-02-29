from rest_framework.viewsets import generics
from formulas.models import Dish, Ingredient, DishIngredientWeight
from formulas.serializers import (
    DishSerializer,
    IngredientSerializer,
    DishIngredientWeightSerializer,
)


class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
